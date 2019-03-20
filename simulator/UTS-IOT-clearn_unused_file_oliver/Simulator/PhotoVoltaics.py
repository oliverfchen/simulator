from PhotoVoltaic import PhotoVoltaic
class PhotoVoltaics:
    pvs = []
    def append(self,pv):
        self.pvs.append(pv)

    def getpvFactorizedPv(self,pvFactor):
        factorizedPVs = []
        for pv in self.pvs:
            newPv = pvFactor * pv.getProduction()
            factorizedPVs.append(PhotoVoltaic(pv.getDate(),pv.getTime(),newPv))
        return factorizedPVs
    def __str__(self):
        strBuffer = ""
        for pv in self.pvs:
            strBuffer = strBuffer + pv.str() + "\n"
        return strBuffer