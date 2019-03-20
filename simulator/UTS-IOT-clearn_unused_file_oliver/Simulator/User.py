# -*- coding: utf-8 -*
from Utils import Utils
class User:

    userId = None
    factorPV = None
    factorC = None
    factorNoiseC = None
    factorNoisePV = None
    pv = []
    userComsumptions = []
    location = None
    def __init__(self,userId,factorPV,factorC,pv,comsumptions,location):
        self.userId = userId
        self.factorPV = factorPV
        self.factorC = factorC
        self.pv = pv
        self.location = location
        # 用户comsumption * factorC
        #print(comsumptions.toString())
        # print(comsumptions.getComsumptions()[0])
        comsumptionsBuff = comsumptions.getComsumptions()
        # print(comsumptionsBuff[0])
        newUserComsumptions = []
        for c in comsumptionsBuff:   
            newC = factorC * c
            newUserComsumptions.append(newC) 
        self.userComsumptions = newUserComsumptions

    def getPv(self):
        return self.pv
    def getPvByIndex(self,index):
        return self.pv[index]
    def getDateTimeByIndex(self,index):
        return "{0} {1}".format(self.pv[index].getDate(),self.pv[index].getTime())
    def getComsumptionByIndex(self,index):
        return self.userComsumptions[index]
    def getComsumptions(self):
        return self.userComsumptions
    def getPrice(self,timeIndex):
        index = timeIndex % 96 
        price = Utils.priceByTime(index)
        return price
    def getPurchase(self,pv,c):
        if(pv.getProduction() > c):
            return 0
        else:
            return c - pv.getProduction()
    def getFeedin(self,pv,c):
        if(pv.getProduction() > c):
            return pv.getProduction() - c
        else:
            return 0
    def getLocation(self):
        return self.location
    def toString(self):
        consuptionBuff = self.comsumptions[10]
        
        return "comsuption{0} ,location {1}\n".format(consuptionBuff,self.location.toString())
    def getUserId(self):
        return self.userId