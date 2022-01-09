#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import torch
# from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
# from keras.preprocessing.sequence import pad_sequences
# from sklearn.model_selection import train_test_split
# from pytorch_pretrained_bert import BertTokenizer, BertConfig
# from pytorch_pretrained_bert import BertAdam, BertForSequenceClassification
# from tqdm import tqdm, trange
# import pandas as pd
# import io
# import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# In[1]:


from sentence_transformers import SentenceTransformer


# In[33]:


class Sentence_Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model_name = model_name
        MAX_LEN = 512
    def embed(self, sentence):
        model = SentenceTransformer(self.model_name)
        sentence_embeddings = model.encode(sentence)
        return sentence_embeddings
        

