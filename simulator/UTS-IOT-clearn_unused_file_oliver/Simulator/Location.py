class Location:
    latitude = None
    longitude = None
    subtown = None
    dsp = None
    def getLatitude(self):
        return self.latitude
    def getLongitude(self):
        return self.longitude
    def getSubtown(self):
        return self.subtown
    def getDsp(self):
        return self.dsp
    def __init__(self, latitude, longitude, subtown, dsp):
        self.latitude = latitude
        self.longitude = longitude
        self.subtown = subtown
        self.dsp = dsp
    def toString(self):
        return "Laititude: {0} longtidue: {1} subtown: {2} dsp: {3}".format(self.latitude,self.longitude,self.subtown,self.dsp)