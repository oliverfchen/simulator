import pandas as csvHelper
from Packet import Packet
import json
from datetime import datetime
import time

class Utils:
    @staticmethod
    def loadCsv(filePath):
        return csvHelper.read_csv(filePath)
    @staticmethod 
    def maxConsumption(profileArray):
        # Max consumption values in each consumption profile, 
        return 0
    @staticmethod
    def priceByTime(time_idx):
        if(time_idx >= 27 and time_idx <= 55 or time_idx >= 80 and time_idx <= 87): 
            return 0.23
        elif(time_idx >= 56 and time_idx <= 79):
            return 0.54
        else:
            return 0.15
    @staticmethod
    def currentTimeToTimeIdx():
        dayofYear = datetime.now().timetuple().tm_yday
        timeIdxOfDay = (dayofYear -1) * 96 
        timeIdxOfHour = datetime.now().timetuple().tm_hour * 4
        timeIdxOfMin = int(datetime.now().timetuple().tm_min / 15)
        timeIdx = timeIdxOfDay + timeIdxOfHour + timeIdxOfMin
        return timeIdx
    @staticmethod
    def timeIdxToTimeStr(timeIdx, year):
        noOfDayOfTimeIdx = int(timeIdx / 96) + 1
        hourOfTimeIdx = int(timeIdx / 4) - int((noOfDayOfTimeIdx-1) * 24)
        minOfTimeIdx = int(timeIdx % 4) * 15
        year = 2018
        yearOfTimeIdx = year
        monthOfTimeIdx = 0
        noOfTotalDays = 0
        if(timeIdx>=0 and timeIdx<2976):
            monthOfTimeIdx = 1
            noOfTotalDays = 0
        elif(timeIdx>=2976 and timeIdx<5664):
            monthOfTimeIdx = 2
            noOfTotalDays = 31
        elif(timeIdx>=5664 and timeIdx<8640):
            monthOfTimeIdx = 3
            noOfTotalDays = 59
        elif(timeIdx>=8640 and timeIdx<11520):
            monthOfTimeIdx = 4
            noOfTotalDays = 90
        elif(timeIdx>=11520 and timeIdx<14496):
            monthOfTimeIdx = 5
            noOfTotalDays = 120
        elif(timeIdx>=14496 and timeIdx<17376):
            monthOfTimeIdx = 6
            noOfTotalDays = 151
        elif(timeIdx>=17376 and timeIdx<20352):
            monthOfTimeIdx = 7
            noOfTotalDays = 181
        elif(timeIdx>=20352 and timeIdx<23328):
            monthOfTimeIdx = 8
            noOfTotalDays = 212
        elif(timeIdx>=23328 and timeIdx<26208):
            monthOfTimeIdx = 9
            noOfTotalDays = 243
        elif(timeIdx>=26208 and timeIdx<29184):
            monthOfTimeIdx = 10
            noOfTotalDays = 273
        elif(timeIdx>=29184 and timeIdx<32064):
            monthOfTimeIdx = 11
            noOfTotalDays = 304
        elif(timeIdx>=32064 and timeIdx<35040):
            monthOfTimeIdx = 12
            noOfTotalDays = 334
        dateOfTimeIdx = noOfDayOfTimeIdx - noOfTotalDays
        finalDateTime = "{0}/{1}/{2}/{3}:{4}".format(yearOfTimeIdx, monthOfTimeIdx, dateOfTimeIdx, hourOfTimeIdx, minOfTimeIdx)
        return finalDateTime
    @staticmethod
    def timeIdxToTime(timeIdx, year):
        noOfDayOfTimeIdx = int(timeIdx / 96) + 1
        hourOfTimeIdx = int(timeIdx / 4) - int((noOfDayOfTimeIdx-1) * 24)
        minOfTimeIdx = int(timeIdx % 4) * 15
        year = 2018
        yearOfTimeIdx = year
        monthOfTimeIdx = 0
        noOfTotalDays = 0
        if(timeIdx>=0 and timeIdx<2976):
            monthOfTimeIdx = 1
            noOfTotalDays = 0
        elif(timeIdx>=2976 and timeIdx<5664):
            monthOfTimeIdx = 2
            noOfTotalDays = 31
        elif(timeIdx>=5664 and timeIdx<8640):
            monthOfTimeIdx = 3
            noOfTotalDays = 59
        elif(timeIdx>=8640 and timeIdx<11520):
            monthOfTimeIdx = 4
            noOfTotalDays = 90
        elif(timeIdx>=11520 and timeIdx<14496):
            monthOfTimeIdx = 5
            noOfTotalDays = 120
        elif(timeIdx>=14496 and timeIdx<17376):
            monthOfTimeIdx = 6
            noOfTotalDays = 151
        elif(timeIdx>=17376 and timeIdx<20352):
            monthOfTimeIdx = 7
            noOfTotalDays = 181
        elif(timeIdx>=20352 and timeIdx<23328):
            monthOfTimeIdx = 8
            noOfTotalDays = 212
        elif(timeIdx>=23328 and timeIdx<26208):
            monthOfTimeIdx = 9
            noOfTotalDays = 243
        elif(timeIdx>=26208 and timeIdx<29184):
            monthOfTimeIdx = 10
            noOfTotalDays = 273
        elif(timeIdx>=29184 and timeIdx<32064):
            monthOfTimeIdx = 11
            noOfTotalDays = 304
        elif(timeIdx>=32064 and timeIdx<35040):
            monthOfTimeIdx = 12
            noOfTotalDays = 334
        dateOfTimeIdx = noOfDayOfTimeIdx - noOfTotalDays
        toConvertDate = "{0}/{1}/{2}/{3}/{4}".format(yearOfTimeIdx, monthOfTimeIdx, dateOfTimeIdx, hourOfTimeIdx, minOfTimeIdx)
        return time.mktime(datetime.strptime(toConvertDate,"%Y/%m/%d/%H/%M").timetuple())

