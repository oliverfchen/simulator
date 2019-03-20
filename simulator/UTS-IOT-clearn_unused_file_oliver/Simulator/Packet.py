import json
import time
import datetime
import paho.mqtt.client as paho
import Config as Config
import Utils

class Packet:
    seq = 0
    @staticmethod
    def on_publish(client,userdata,result):             #create function for callback MQTT
        #print("data published \n")
        pass
        return
    @staticmethod
    def mqtt_send(json_data):
        broker = Config.HOST_ADDR
        port= Config.HOST_PORT
        client1= paho.Client(Config.HOST_CLIENT)                           #create client object
        client1.on_publish = Packet.on_publish                          #assign function to callback
        client1.connect(broker,port)  #establish connection
        message = json.dumps(json_data)
        # ret=client1.publish("PV_data_feed_In",message) 
        ret=client1.publish("house",message) 
        if ret[0] != 0:        
            time.sleep(0.5)
        else:
            time.sleep(0.1)
    @staticmethod 
    def printServerInfo():
        print("Send data to: {0}:{1}".format(Config.HOST_ADDR,Config.HOST_PORT))
    @staticmethod 
    def sendPacket(user,timeIndex):
        user_id = user.getUserId()
        pv = user.getPvByIndex(timeIndex)
        c = user.getComsumptionByIndex(timeIndex)
        consumption = user.getComsumptionByIndex(timeIndex)
        production = user.getPvByIndex(timeIndex).getProduction()
        purchase = user.getPurchase(pv,c)
        feed_in = user.getFeedin(pv,c)
        dsp = user.getLocation().getDsp()
        latitude = user.getLocation().getLatitude()
        longitude = user.getLocation().getLongitude()
        subtown = user.getLocation().getSubtown()
        user_price = user.getPrice(timeIndex)
        date_time = datetime.datetime.strptime(user.getDateTimeByIndex(timeIndex),"%Y/%m/%d %H:%M:%S")
        #data = "datetime_int: {0}, comsumption: {1}, production: {2}, purchase: {3}, feedin: {4}, price {5}, location {6}".format('unknown',user.getComsumptionByIndex(timeIndex),user.getPvByIndex(timeIndex).getProduction(),user.getPurchase(pv,c),user.getFeedin(pv,c),user.getPrice(timeIndex),user.getLocation().toString())
        Packet.seq = Packet.seq + 1
        
        data = {
            "key": Packet.seq,
            #"date_time":date_time.timestamp(),
            "date_time":datetime.datetime.now().strftime("%s"),
            "user_id": user_id,
            "consumption": consumption,
            "pv_generation": production,
            "purchase": purchase,
            "feed_in": feed_in,
            "DSP": dsp,
            "latitude": latitude,
            "longitude": longitude,
            "subtown": subtown,
            "user_price": user_price
        }
        
        # print("{0}\n".format(serverAddr))
        Packet.mqtt_send(data)
        #print(datetime.datetime.strptime(user.getDateTimeByIndex(timeIndex),"%Y/%m/%d %H:%M:%S"))
        print(data)
    @staticmethod 
    def sendPacketHistory(user,timeIndex):
        user_id = user.getUserId()
        pv = user.getPvByIndex(timeIndex)
        c = user.getComsumptionByIndex(timeIndex)
        consumption = user.getComsumptionByIndex(timeIndex)
        production = user.getPvByIndex(timeIndex).getProduction()
        purchase = user.getPurchase(pv,c)
        feed_in = user.getFeedin(pv,c)
        dsp = user.getLocation().getDsp()
        latitude = user.getLocation().getLatitude()
        longitude = user.getLocation().getLongitude()
        subtown = user.getLocation().getSubtown()
        user_price = user.getPrice(timeIndex)
        date_time = datetime.datetime.strptime(user.getDateTimeByIndex(timeIndex),"%Y/%m/%d %H:%M:%S")
        #data = "datetime_int: {0}, comsumption: {1}, production: {2}, purchase: {3}, feedin: {4}, price {5}, location {6}".format('unknown',user.getComsumptionByIndex(timeIndex),user.getPvByIndex(timeIndex).getProduction(),user.getPurchase(pv,c),user.getFeedin(pv,c),user.getPrice(timeIndex),user.getLocation().toString())
        Packet.seq = Packet.seq + 1
        
        data = {
            "key": Packet.seq,
            #"date_time":date_time.timestamp(),
            "date_time":Utils.Utils.timeIdxToTime(timeIndex, 2018),
            "user_id": user_id,
            "consumption": consumption,
            "pv_generation": production,
            "purchase": purchase,
            "feed_in": feed_in,
            "DSP": dsp,
            "latitude": latitude,
            "longitude": longitude,
            "subtown": subtown,
            "user_price": user_price
        }
        
        # print("{0}\n".format(serverAddr))
        Packet.mqtt_send(data)
        #print(datetime.datetime.strptime(user.getDateTimeByIndex(timeIndex),"%Y/%m/%d %H:%M:%S"))
        print(data)