from search import Search
"""
模拟退火解决针对100个工件的单机极小化总流水时间的排序问题
文件名:sa.py
author:NearlyHeadlessJack@rjack.cn
comment:程序入口
"""

def main():
    search = Search(temp0=300,temp=400,r=0.98,deltaT=4,isDelta=True,inner_count=5)
    search.exp1()


if __name__ == '__main__':
    main()