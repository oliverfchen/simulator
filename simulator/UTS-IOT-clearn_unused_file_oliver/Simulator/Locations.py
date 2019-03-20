import random
class Locations:
    locs = []
    selectedIdxs = []
    def append(self,loc):
        self.locs.append(loc)
    def getLocs(self):
        return self.locs
    def random(self):
        choosedIdx = random.choice(range(0,len(self.locs)-1))
        if(self.isChoosed(choosedIdx)) : self.random()
        else: self.selectedIdxs.append(choosedIdx)
        return self.locs[choosedIdx]
    
    def isChoosed(self,idx):
        for id in self.selectedIdxs:
            if(id == idx):
                 return True
            else:
                return False
         
    def toString(self):
        strBuffer = ""
        for loc in self.locs:
            strBuffer += loc.toString()
        return strBuffer