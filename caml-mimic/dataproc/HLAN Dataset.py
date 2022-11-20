# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:09:47 2022

@author: ben-p
"""

from torch.utils.data.dataset import Dataset
import pandas as pd

train_50 = pd.read_csv('C:/Users/ben-p/.spyder-py3/CSE6250 HLAN Project/Data/train_50.csv')

class dataset(Dataset):
    def __init__(self,filepath):
        self.data = pd.read_csv(filepath)
        
        
    def __len__(self):
      return len(self.data)
    
    
    def __getitem__(self, index):
      return self.data[index], self.data['LABELS'][index]   