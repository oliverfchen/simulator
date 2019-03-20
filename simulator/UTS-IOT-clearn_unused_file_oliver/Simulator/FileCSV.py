import Config as Config
from User import User
import datetime
import pandas as pd
import Utils


class FileCSV:

    @staticmethod 
    def overwriteCsv():
        
        csv = open("simResults.csv","w+")
        csv.write("user_id,date_time,purchase,feed_in,consumption,pv_generation,DSP,latitude,longitude,subtown,user_price\r\n")
        csv.close()

    @staticmethod
    def csv_feedin_purchase_1(user, timeIndex):
        user_id = user.getUserId()
        pv = user.getPvByIndex(timeIndex)
        c = user.getComsumptionByIndex(timeIndex)
        consumption = user.getComsumptionByIndex(timeIndex)
        production = user.getPvByIndex(timeIndex).getProduction()
        purchase = user.getPurchase(pv, c)
        feed_in = user.getFeedin(pv, c)
        dsp = user.getLocation().getDsp()
        latitude = user.getLocation().getLatitude()
        longitude = user.getLocation().getLongitude()
        subtown = user.getLocation().getSubtown()
        user_price = user.getPrice(timeIndex)
        date_time = datetime.datetime.strptime(
            user.getDateTimeByIndex(timeIndex), "%Y/%m/%d %H:%M:%S")

        data = {
            # "date_time":date_time.timestamp(),
            "user_id": user_id,
            "date_time": [Utils.Utils.timeIdxToTimeStr(timeIndex, 2018)],
            "purchase": [purchase],
            "feed_in": [feed_in],
            "consumption": [consumption],
            "pv_generation": [production],
            "DSP": dsp,
            "latitude": [latitude],
            "longitude": [longitude],
            "subtown": [subtown],
            "user_price": [user_price]
        }
        #print("write to file:\n")
        #print(data)
        df = pd.DataFrame(data )
        df.to_csv('simResults.csv', mode='a',index = False, header=None)
