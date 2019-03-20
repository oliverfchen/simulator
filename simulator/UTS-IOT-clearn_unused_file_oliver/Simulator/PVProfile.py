# -*- coding: utf-8 -*
class PVProfile:
    date = None
    production = None
    time = None

    def __init__(self,date,production,time):
        self.date = date
        self.production = production
        self.time = time
    
    # 重载父类 ToString方法
    def __str__(self):
        return "Date:{0} Time: {1} Production: {2}".format(self.date,self.time,self.production)