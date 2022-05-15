from copy import deepcopy
import numpy as np
from numpy import dot
import copy
"""
文件名:data.py
author:NearlyHeadlessJack@rjack.cn
comment:数据产生类
"""

class Data:
    #初始化随机生成数据
    def __init__(self):
        self.product = np.random.randint(20,101,size=(1,100))
        # self.product = np.arange(100,0,-1)
        # self.product.shape = 1,100
        self.best = copy.deepcopy(self.product)
        self.now = copy.deepcopy(self.product)
        self.temp = copy.deepcopy(self.product)
        self.count = np.arange(100,0,-1)
        self.best_result = dot(self.product,self.count)
        self.now_result = dot(self.product,self.count)
        return
    
    # 恢复数据至初始状态
    def reset(self):
        self.best = copy.deepcopy(self.product)
        self.now = copy.deepcopy(self.product)
        self.temp = copy.deepcopy(self.product)
        self.count = np.arange(100,0,-1)
        self.best_result = dot(self.product,self.count)
        self.now_result = dot(self.product,self.count)
        
    # 计算当前值
    def calculate(self,order):
        order = dot(order,self.count)
        return order
    
    # 更新最优值
    def update_best(self):
        self.best = copy.deepcopy(self.now)
        self.best_result = dot(self.best,self.count)
        
    # opt-2随机领域移动  只移动temp 是否接受移动由内循环决定
    def random_change(self):
        self.temp = copy.deepcopy(self.now)
        a = np.random.randint(0,100)
        b = np.random.randint(0,100)
        while b==a:
            b = np.random.randint(0,100)
        self.temp[0][a],self.temp[0][b] = self.temp[0][b],self.temp[0][a]
        
    
    
    
    