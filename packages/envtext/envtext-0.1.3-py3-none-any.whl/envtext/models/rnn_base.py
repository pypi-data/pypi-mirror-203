from .model_base import ModelBase
import torch
from torch.utils.data import TensorDataset,DataLoader
from transformers.configuration_utils import PretrainedConfig
from ..tokenizers import Word2VecTokenizer,OnehotTokenizer,TFIDFTokenizer
from tqdm import tqdm
from collections import defaultdict
import numpy as np
import os

class RNNBase(ModelBase):
    def __init__(self,path = None, config = None,model_name = 'lstm', labels = [],num_labels = 0, entities = [],num_entities = 0, ner_encoding = 'BIO' , \
                     max_length = 128, hidden_size = 512 ,num_layers = 3, onehot_embed = False, embed_size = 512, token_method = 'word2vec', \
                    word2vec_path = None,vocab_path = None, truncation = True,padding=True, remake_vocab= True,**kwargs):
        '''
        RNN模型
        
        Args:
            path [Optional] `str` : 默认None
                模型导入的文件夹路径
                如果是None，则暂时不导入模型。
           
            config [Optional] `dict` : 默认 None
                模型的配置参数，以dict的方式传入，可以选择的参数见Kwargs
                如果是None，则初始化一个空的config
        
        Kwargs:
            Kwargs中都是模型的配置参数。
            
            model_name [Optional] `str`: 默认'LSTM'
                模型的名称，可以选择'lstm','rnn','gru'三者之一。
                模型默认是双向(bidirectional)的。
            
            labels [Optional] `List[int]` or `List[str]`: 默认None
                分类问题中标签的种类。
                分类问题中和num_labels必须填一个，代表所有的标签。
                如果是RNNCLS模型，默认为['LABEL_0','LABEL_0']
                如果是RNNMultiChoice模型，默认为['LABEL_0']
           
            num_labels [Optional] `int`: 默认None
                分类问题中标签的数量。
                分类问题中和num_labels必须填一个，代表所有的标签。
                如果是RNNCLS模型，默认为2
                如果是RNNMultiChoice模型，默认为1 
                
           entities [Optional] `List[int]` or `List[str]`: 默认为None
               命名实体识别问题中实体的种类。
               命名实体识别问题中与entities/num_entities必填一个。
               实体使用BIO标注，如果n个实体，则有2*n+1个label。
               eg:
                   O: 不是实体
                   B-entity1：entity1的实体开头
                   I-entity1：entity1的实体中间
                   B-entity2：entity2的实体开头
                   I-entity2：entity2的实体中间
           
           num_entities [Optional] `int`: 默认None
               命名实体识别问题中实体的数量。
               命名实体识别问题中与labels/num_labels/entities必填一个。
               实体使用BIO标注，如果n个实体，则有2*n+1个label。
          
           max_length [Optional] `int`: 默认：128
               支持的最大文本长度。
               如果长度超过这个文本，则截断，如果不够，则填充默认值。
               
           hidden_size [Optional] `int`: 默认：512
               模型隐藏层向量维度大小。
               
           num_layers [Optional] `int`: 默认：3
               RNN模型的层数
               
            onehot_embed[Optional] `bool`: 默认：False
                使用onehot编码时会自动设置为True，在模型中添加一层embedding layer

           embed_size [Optional] `int`: 默认：512
               模型嵌入向量的大小。
               只有当token_method == onehot时会启用。
               当token_method == word2vec时，词向量已经默认设置为64维。
               
           token_method [Optional] `str`: 默认：'word2vec'
                将文本转换为向量的方法：
                    'word2vec': 使用预训练的词向量
                    'onehot': 使用onehot向量
        '''
        super().__init__()
        self.train_reports = defaultdict(list)
        self.valid_reports = defaultdict(list)
        self.optim = None
        self.schedule = None
        self.model = None
        
        

        if path is None:
            self.update_config(
                model_name = model_name,
                labels = labels,
                num_labels = num_labels,
                entities = entities,
                num_entities = entities,
                ner_encoding = ner_encoding,
                max_length = max_length, 
                hidden_size = hidden_size,
                num_layers = num_layers, 
                onehot_embed = onehot_embed,
                embed_size = embed_size,
                token_method = token_method,
                word2vec_path = word2vec_path,
                vocab_path = vocab_path,
                truncation = truncation,
                padding = padding,
                remake_vocab = remake_vocab,
                **kwargs
            )

        self.initialize_config(path = path, **kwargs)

        self.initialize_tokenizer(path = path,**kwargs)

        self.initialize_rnn(path=path,**kwargs)
        
        if self.model:
            self.model = self.model.to(self.device)
        
    
    def initialize_tokenizer(self,path = None,**kwargs):
        '''
        初始化tokenizer:
       
        Args:
            token_method [Optional] `str`: 默认： None
                将文本转换为向量的方法：
                    'word2vec': 词向量
                    'onehot': onehot向量
        '''
        self.update_config(**kwargs)        
        
        vocab_path = self.config.vocab_path
        if not vocab_path and path:
            if "vocab.txt" in os.listdir(path):
                vocab_path = os.path.join(path,"vocab.txt")

        if self.token_method == "onehot":
            self.tokenizer = OnehotTokenizer(max_length = self.max_length,padding=self.config.padding,truncation=self.config.truncation,vocab_path= vocab_path) 
        elif self.token_method == "tf-idf":
            self.tokenizer = TFIDFTokenizer(max_length = self.max_length,padding=self.config.padding,truncation=self.config.truncation,vocab_path= vocab_path,split = self.config.split)
        else:
            self.update_config(token_method = "word2vec")
            self.tokenizer = Word2VecTokenizer(max_length = self.max_length,padding=True,truncation=True,word2vec_path=self.config.word2vec_path) 
        

        if self.token_method == "onehot":
            self.set_attribute(onehot_embed = True)
        
    def initialize_config(self,path = None, **kwargs):
        '''
        初始化配置参数config
         
         Args：
             path [Optional] `str`: 默认None
                 默认从path中导入config.json文件
                 如果path不存在，则初始化一个空的PretrainedConfig()
        '''
        if path is not None:
            config = PretrainedConfig.from_pretrained(path)
            self.config.update(config)
            
        self.config.update(kwargs)
    
    def align_config(self):
        '''
        对齐config，在initialize_rnn的时候调用，如有必要则进行重写。
        '''
        pass
    



    def initialize_rnn(self,path = None,config = None,**kwargs):
        '''
        需要继承之后重新实现
        '''
        self.update_model_path(path)
        self.update_config(config)
        self.update_config(kwargs)
        self.align_config()
        if path is not None:
            if os.path.exists(os.path.join(path,'pytorch_model.bin')):
                self.load(path)

        if self.datasets and self.token_method in ["onehot","tf-idf"] and self.config.remake_vocab:
            for k,v in self.datasets.items():
                import re
                lines =[re.sub("\s","",vv) for vv in v["text"]]
                self.tokenizer.make_vocab(lines)

    
    def update_model_path(self,path):
        '''
        更新模型路径
       Args:
           path `str`:
               模型新的路径
        '''
        if path is not None:
            self.config._name_or_path = path
        
        
    @property
    def model_path(self):
        '''
        获得模型路径，没有路径则返回None
        '''
        if hasattr(self.config,'_name_or_path'):
            return self.config._name_or_path
        else:
            return None

    @property
    def model_name(self):
        '''
        获得模型名称
        '''
        if hasattr(self.config,'model_name'):
            return self.config.model_name
        else:
            return None

    @property
    def max_length(self):
        '''
        获得最大长度
        '''
        if hasattr(self.config,'max_length'):
            return self.config.max_length
        else:
            return None
        
    @property
    def token_method(self):
        '''
        获得模型路径，没有路径则返回None
        '''
        if hasattr(self.config,'token_method'):
            return self.config.token_method
        else:
            return None
        
    @property
    def label2id(self):
        '''
        返回一个dict,标签转id
        '''
        if hasattr(self.config,'label2id'):
            return self.config.label2id
        else:
            return None
        
    @property
    def id2label(self):
        '''
        返回一个dict,id转标签
        '''
        if hasattr(self.config,'id2label'):
            return self.config.id2label
        else:
            return None
        
    @property
    def labels(self):
        '''
        返回一个list,所有标签
        '''
        if hasattr(self.config,'labels'):
            return self.config.labels
        else:
            return None

    @property
    def num_labels(self):
        '''
        返回一个list,所有标签
        '''
        if hasattr(self.config,'num_labels'):
            return self.config.num_labels
        else:
            return None

    @property
    def num_entities(self):
        '''
        返回一个list,所有标签
        '''
        if hasattr(self.config,'num_entities'):
            return self.config.num_entities
        else:
            return None
        
    @property
    def entities(self):
        '''
        返回一个list,所有实体
        '''
        if hasattr(self.config,'entities'):
            return self.config.entities   
        else:
            return None
    
    def get_train_reports(self):
        '''
        获得训练集metrics报告
        '''
        return self._report(self.train_reports)
    
    def get_valid_reports(self):
        '''
        获得验证集metrics报告
        '''
        return self._report(self.valid_reports)
    
    def set_optim(self,optim, learning_rate = 1e-3):
        '''
        设置优化器，
        Args:
            optim `str` or `torch.optim`:
                默认是Adam优化器，learning rate在训练时传入
                用此接口设置优化器后，不必传入learning rate
                optim == 'SDG': 
                    使用SDG with momentum优化器
                optim == 'Adam':
                    使用Adam优化器
        '''
        self.optim = optim
        
    def set_learing_rate_schedule(self,schedule):
        '''
        设置学习率迭代方法，默认是torch.optim.lr_scheduler.CosineAnnealingLR
        '''
        self.schedule = schedule
    
    def load_checkpoint(self,path):
        '''
        从checkpoint导入模型，但是必须要重新设置
        '''
        checkpoint = torch.load(path)
        self.model = checkpoint['best_model'].to(self.device)
        print('epoch number and learning rate of checkpoint is {} and {:.4e}'.format(checkpoint['epoch'],checkpoint['learning rate']))
        

    def load(self,path):
        '''
        Args:
            path `str`:
                模型pytorch_model.bin所在文件夹
        '''
        if os.path.exists(os.path.join(path,'pytorch_model.bin')):
            self.model = torch.load(os.path.join(path,'pytorch_model.bin'))
            self.model = self.model.to(self.device)
            print("RNN模型导入成功")
        else:
            print("请输入正确的文件夹，确保文件夹里面含有pytorch_model.bin文件")
        
              
    def _update_train_reports(self,report):
        for k,v in report.items():
            self.train_reports[k].append(v)

    def _update_valid_reports(self,report):
        for k,v in report.items():
            self.valid_reports[k].append(v)
            
    def _tokenizer_for_training(self,texts, desc = "Tokenizing进度"):
        tokens = []
        for text in tqdm(texts,desc = desc):
            tokens.append(self.tokenizer(text)[0])
        tokens = torch.from_numpy(np.array(tokens,dtype=np.float32))
        return tokens
    
    def _train_per_step(self,train_dataloader):
        self.model.train()
        bar = tqdm(train_dataloader)
        preds,labels,losses = [],[],[]
        for X,label in bar:
            #move to device
            X = X.to(self.device)
            label = label.to(self.device)
            #更新模型参数
            self.optim.zero_grad()
            loss,predict = self.model(X,label)
            loss.backward()
            self.optim.step()
            self.schedule.step()
            #打印报告
            preds.append(predict.clone().detach().cpu().numpy())
            labels.append(label.clone().detach().cpu().numpy())
            losses.append(loss.clone().detach().cpu().item())
            bar.set_description("Train Loss is {:.4f}".format(losses[-1]))
        preds = np.concatenate(preds,axis = 0)
        labels = np.concatenate(labels,axis = 0)
        loss = sum(losses)/len(bar)
        
        report = self.compute_metrics((preds,labels))
        if isinstance(report,dict):
            report['training loss'] = loss
        elif isinstance(report,float):
            report = {'metric':report,'training loss':loss}
        else:
            report = {'training loss':loss}
        return report

    def _valid_per_step(self,train_dataloader):
        self.model.eval()
        bar = tqdm(train_dataloader)
        preds,labels,losses = [],[],[]
        for X,label in bar:
            X = X.to(self.device)
            label = label.to(self.device)
            loss,predict = self.model(X,label)
            preds.append(predict.clone().detach().cpu().numpy())
            labels.append(label.clone().detach().cpu().numpy())
            losses.append(loss.clone().detach().cpu().item())
            bar.set_description("Valid Loss is {:.4f}".format(losses[-1]))
        
        preds = np.concatenate(preds,axis = 0)
        labels = np.concatenate(labels,axis = 0)
        loss = sum(losses)/len(bar)
        
        report = self.compute_metrics((preds,labels))
        if isinstance(report,dict):
            report['validation loss'] = loss
        elif isinstance(report,float):
            report = {'metric':report,'validation loss':loss}
        else:
            report = {'validation loss':loss}
        return report

    def _inference_per_step(self,dataloader):
        self.model.eval()
        preds = []
        for X in tqdm(dataloader,desc="正在 Inference ..."):
            X = X.to(self.device)
            with torch.no_grad():
                predict = self.model(X)[0]
            preds.append(predict.clone().detach().cpu().numpy())
            
        preds = np.concatenate(preds,axis = 0)
        return preds    
    
    @torch.no_grad()
    def inference(self, texts = None, batch_size = 2):
        '''
        推理数据集，更快的速度，更小的cpu依赖，建议大规模文本推理时使用。
        与self.predict() 的区别是会将数据打包为batch，并使用gpu进行预测，最后再使用self.postprocess()进行后处理，保存结果至self.result
        
        texts (`List[str]`): 数据集
            格式为列表
            
        '''
        texts = self._align_input_texts(texts)
        
        #模型
        self.model = self.model.to(self.device)
        
        #准备数据集
        input_ids = self._tokenizer_for_training(texts,dece = "推理 Tokenizing 进度")
        dataset = TensorDataset(input_ids)
        dataloader = DataLoader(dataset,batch_size = batch_size, shuffle = False,drop_last = False)
        
        #推理
        preds = self._inference_per_step(dataloader)
        
        #保存results获得
        for text,pred in tqdm(zip(texts,preds),desc="正在后处理..."):
            self.postprocess(text,pred,print_result = False,save_result = True)
        
        
    def train(self,my_datasets = None, epoch = 3 ,batch_size = 2 , learning_rate = 1e-3 ,save_path = None ,checkpoint_path = None,**kwargs):
        '''
        Args:
             my_datasets (`dict`): 数据集
                 格式为: {'train':{'text':[],'label':[]},'valid':{'text':[],'label':[]}}
                 
             epoch (`int`): epoch数量
                 遍历数据集数量，一般是3-10遍
                 
             batch_size (`int`): 批大小
                 一般batch_size越大越好，但是如果太大会超出内存/显存容量，常用的batch_size为4-32
                 
             save_path (`str`): 模型保存位置
                 会写入save_path指定的文件夹，模型名称为pytorch_model.bin
                 
             checkpoint_path (`str`): 检查点保存的位置
                 会写入checkpoint_path指定的文件夹
        '''   
        #模型
        self.model = self.model.to(self.device)
        
        #准备数据集
        if my_datasets is None:
            my_datasets = self.datasets
            
        train_dataset = TensorDataset(
            self._tokenizer_for_training(my_datasets['train']['text'],desc = "训练集 Tokenizing 进度"),
            torch.tensor(my_datasets['train']['label'])
            )
        valid_dataset = TensorDataset(
            self._tokenizer_for_training(my_datasets['valid']['text'],desc = "验证集 Tokenizing 进度"),
            torch.tensor(my_datasets['valid']['label'])
            )   
        
        train_dataloader = DataLoader(train_dataset,batch_size = batch_size, shuffle = True,drop_last = False)
        valid_dataloader = DataLoader(valid_dataset,batch_size = batch_size, shuffle = False,drop_last = False)
        
        #优化器
        if self.optim is None:
            self.optim = torch.optim.Adam(self.model.parameters() ,lr = learning_rate)
        if self.schedule is None:
            self.schedule = torch.optim.lr_scheduler.CosineAnnealingLR(self.optim,T_max= epoch * len(train_dataloader),eta_min = 1e-7)    
        
        #训练
        print("*"*7,"  开始训练  ","*"*7)
        for i in range(epoch):
            train_report = self._train_per_step(train_dataloader)
            self._update_train_reports(train_report)
                
            valid_report = self._valid_per_step(valid_dataloader)
            self._update_valid_reports(valid_report)

            self._report(valid_report)
            
            metric = self.key_metric if self.key_metric in valid_report.keys() else 'validation loss'
            
            if i == 0:
                self._best_metric = valid_report[metric]
                self._best_model = self.model
            else:
                if self.key_metric.find('loss') != -1 and valid_report[metric] < self._best_metric:
                    self._best_model = self.model
                elif valid_report[metric] > self._best_metric:
                    self._best_model = self.model
                else:
                    pass
            if checkpoint_path:
                if not os.path.exists(checkpoint_path):
                    os.makedirs(checkpoint_path)
                checkpoint = {'epoch':i,
                          'learning rate': self.optim.state_dict()['param_groups'][0]['lr'],
                           'best_model':self._best_model}
                torch.save(checkpoint,os.path.join(checkpoint_path,f'checkpoint_e{i}.pt'))
        
        self.model = self._best_model
        
        del self._best_model
        
        if save_path:
            self.save_model(save_path)
    
    @torch.no_grad()
    def eval(self,my_dataset,batch_size):
        #模型
        self.model = self.model.to(self.device)
        
        #准备数据集
        if my_datasets is None:
            if len(self.datasets["test"]["text"]) == 0:
                my_datasets = self.datasets["valid"]
                print("没有test数据集，使用valid数据验证")
            else:
                my_datasets = self.datasets["test"]

        eval_dataset = TensorDataset(
            self._tokenizer_for_training(my_datasets['text'],desc = "测试集 Tokenizing 进度"),
            torch.tensor(my_datasets['label'])
            )
        
        eval_dataloader = DataLoader(eval_dataset,batch_size = batch_size, shuffle = False,drop_last = False)
        
        eval_report = self._valid_per_step(eval_dataloader)
        self._report(eval_report)


    def load_dataset(self,*args,**kwargs):
        '''
        读取数据集。
          参见 envText.data.utils.load_dataset
        
        Args:
            path `str`:
                数据集的路径
                
            task `str`:
                任务名称：
                分类任务：'cls','classification','CLS','class'
                回归任务：'reg'，'regression','REG'
                情感分析：'sa','SA','Sentimental Analysis'
                命名实体识别：'ner','NER','namely entity recognition'
                多选：'MC','mc','multi-class','multi-choice','mcls'
                关键词识别：'key word','kw','key_word'
                
           format `str`:
               格式：详细见envText.data.utils.load_dataset的注释
               - json: json的格式
                   {'train':{'text':[],'label':[]},'valid':{'text':[],'label':[]}}
                   或 {'text':[],'label':[]}
               - json2:json的格式，但是label作为key
                   {'train':{'label1':[],'label2':{},...},'valid':{'label1':[],'label2':{},...}}
                   或 {'label1':[],'label2':{},...}
               - text: 纯文本格式，一行中同时有label和text
                       text label datasets
                       text1 label1 train
                       text2 label2 valid
                       ...
                   或
                       text label
                       text1 label1
                       text2 label2
                       ...
                   或
                       train
                       text1 label1
                       text2 label2
                       ...
                       valid
                       text1 label1
                       text2 label2
                       ...
    
               - text2:纯文本格式，一行text，一行label
                       train
                       text1
                       label1
                       ...
                       valid
                       text2
                       label2
                       ...
                    或：
                       text1
                       label1
                       text2
                       label2
               - excel: excel,csv等格式
                  |text | label | dataset |
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| valid |
                  |text3| label3| test |
                  或
                  |text | label | 
                  | --- | ---  | 
                  |text1| label1|
                  |text2| label2|
                  |text3| label3|
       Kwargs:   
         
         split [Optional] `float`: 默认：0.5
               训练集占比。
               当数据集没有标明训练/验证集的划分时，安装split:(1-split)的比例划分训练集:验证集。
               
          sep [Optional] `str`: 默认：' '
               分隔符：
               text文件读取时的分隔符。
               如果keyword、ner任务中，实体标注没有用list分开，而是用空格或逗号等相连，则sep作为实体之间的分隔符。
               例如：有一条标注为
                   "气候变化,碳中和"，设置sep=','，可以将实体分开
                   一般建议数据集格式为["气候变化","碳中和"]，避免不必要的混淆
                   
          label_as_key `bool`: 默认：False
              如果格式为json且设置label_as_key，等效于json2格式
          
          dataset `str`: 默认：'dataset'
              标示数据集一列的列头。
              例如csv文件中：
                  |text | label | **dataset **|
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| valid |
                  |text3| label3| test |
                  
          
          train `str`: 默认：'train'
              标示数据是训练/验证集/测试集
            例如csv文件中：
                  |text | label | dataset|
                  | --- | ---  | ------ |
                  |text1| label1| **train** |
                  |text2| label2| valid |
                  |text3| label3| test |
         
         valid `str`: 默认：'valid'
              标示数据是训练/验证集/测试集
            例如csv文件中：
                  |text | label | dataset|
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| **valid** |
                  |text3| label3| test |
         
         
         test `str: 默认：'test'
           标示数据是训练/验证集/测试集
            例如csv文件中：
                  |text | label | dataset|
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| valid |
                  |text3| label3| **test** |
          
         text `str`: 默认：'text'
            标示文本列的列头
            例如csv文件中：
                  |**text** | label | dataset|
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| valid |
                  |text3| label3| test  |
                  
         label `str`: 默认：'label'
            标示标签列的列头
            例如csv文件中：
                  |text | **label** | dataset|
                  | --- | ---  | ------ |
                  |text1| label1| train |
                  |text2| label2| valid |
                  |text3| label3| test  |
        '''
        super().load_dataset(*args,**kwargs)
        self.initialize_rnn( None, self.data_config)