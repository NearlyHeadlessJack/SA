"""
文件名:savedata.py
author:NearlyHeadlessJack@rjack.cn
comment:保存文件用的类
"""
class SaveData:
    def __init__(self) :
        self.exp_index = []
        self.exp_temp0 = []
        self.exp_temp = []
        self.exp_deltaT = []
        self.exp_inner_count = []
        self.exp_best = []
        return 
    
    def save(self,index,temp0,temp,deltaT,inner_count,best):
        self.exp_index.append(index)
        self.exp_temp0.append(temp0)
        self.exp_temp.append(temp)
        self.exp_deltaT.append(deltaT)
        self.exp_inner_count.append(inner_count)
        self.exp_best.append(best)
        
        
        
    def write_data(self):     
        with open(file = 'index.txt',mode = 'w+')as f:
            for exp in self.exp_index:
                f.writelines(str(exp)+'\n') 
        with open(file = 'temp0.txt',mode = 'w+')as f:
            for exp in self.exp_temp0:
                f.writelines(str(exp)+'\n') 
        with open(file = 'temp.txt',mode = 'w+')as f:
            for exp in self.exp_temp:
                f.writelines(str(exp)+'\n')
        with open(file = 'deltaT.txt',mode = 'w+')as f:
            for exp in self.exp_deltaT:
                f.writelines(str(exp)+'\n')
        with open(file = 'inner_count.txt',mode = 'w+')as f:
            for exp in self.exp_inner_count:
                f.writelines(str(exp)+'\n')
        with open(file = 'best.txt',mode = 'w+')as f:
            for exp in self.exp_best:
                f.writelines(str(exp[0])+'\n')
                
                
                
    