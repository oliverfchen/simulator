class Comsumption:
    comsumptions = []
    def __init__(self,comsumptions):
        self.comsumptions = comsumptions 

    def appendComsumption(self,value):
        self.comsumptions.append(value / 3.0)     #was 3000.0

    def getComsumptions(self):
        return self.comsumptions
    def toString(self):
        comsumptionBuff = ""
        for data in self.comsumptions:
            comsumptionBuff += str(data)
        return "comsumptions {0} \n".format(comsumptionBuff)
