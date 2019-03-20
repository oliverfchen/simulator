# -*- coding: utf-8 -*
import random
# from Config import Config 
class Comsumptions:
    comsumptions = [] # 24 个文件,随机取一个

    def append(self,comsumption):
        self.comsumptions.append(comsumption)
    def random(self):
        choosedIdx = random.choice(range(0,len(self.comsumptions)-1))
        # print("分配到comsumption ->{0}".format(choosedIdx))
        return self.comsumptions[choosedIdx]
    def getComsumptions(self):
        return self.comsumptions

    def __str__(self):
        strBuff = ""
        for con in self.comsumptions: 
            strBuff += con.toString()
        return strBuff

    def toString(self):
        strBuff = ""
        for con in self.comsumptions: 
            strBuff += con.toString()
        return strBuff