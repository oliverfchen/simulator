class PhotoVoltaic:
    time = None
    date = None
    production = None
    def getTime(self):
        return self.time
    def getDate(self):
        return self.date
    def getProduction(self):
        return self.production
    def setProduction(self,newProduction):
        self.production = newProduction
    def __init__ (self,date,time,production):
        self.date = date
        self.time = time
        self.production = (production)

    def __str__(self):
        return "time: {0}, date: {1} production: {2}".format(self.time,self.date,self.production)

    
    def str(self):
        return "time: {0}, date: {1} production: {2}".format(self.time,self.date,self.production)

    