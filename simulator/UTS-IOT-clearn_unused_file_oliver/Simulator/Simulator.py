# -*- coding: utf-8 -*
import Config as Config
from Utils import Utils
from PhotoVoltaic import PhotoVoltaic
from PhotoVoltaics import PhotoVoltaics
from Comsumptions import Comsumptions
from Comsumption import Comsumption
from User import User
from Users import Users
from Locations import Locations
from Location import Location
from Packet import Packet
from FileCSV import FileCSV
import os
import sys
import random
from matplotlib import pyplot as chart
import json
import datetime
import time
class Simulator:
	photoVoltaics = PhotoVoltaics()
	comsumptions = Comsumptions()
	users = Users()
	locations = Locations()
	totalNoUsers = 10
	# File Handle
	profileCSV = None
	def setup(self):
		print(Config.C_NORMAL+"Program Initialization...")
		# Load files
		self.loadFile()
		# Generate user data
		self.generateUsers()
		print("Initialization finished"+Config.C_VAUE+"=w="+Config.C_NORMAL)

	def loadFile(self):
		print("Load Location CSV files...")
		locationsCSV = Utils.loadCsv(Config.LOCATION_PROFILE_FILEPATH)
		print("Load Location CSV finished\nCreating location data...")
		for subtowm,latitude,longitude,dsp in zip(locationsCSV.neighbourhood,locationsCSV.latitude,locationsCSV.longitude,locationsCSV.DSP):
			self.locations.append(Location(latitude,longitude,subtowm,dsp))
		print("Location load finish.")

		print("Load PV CSV files...")
		self.profileCSV = Utils.loadCsv(Config.PV_PROFILE_CSV_FILEPATH)
		# Create & Load PV data
		print("PV file load finished\nCreating PV data...")
		for date,production,time in zip(self.profileCSV.date,self.profileCSV.production,self.profileCSV.time):
			self.photoVoltaics.append(PhotoVoltaic(date,time,production))
		# print(self.profileCSV.iloc[0,0])
		# Create & Load Comsumption data
		print("Load Comsumptions file...")
		comsuptionsFileCount = 0
		comsuptionsDataCount = 0 
		for filename in os.listdir(Config.CONSUMPTION_PROFILE_FILEPATH):
			file = Utils.loadCsv(Config.CONSUMPTION_PROFILE_FILEPATH+filename)
			print("Processing File:"+Config.C_VAUE+"{0}...".format(filename)+Config.C_NORMAL)
			comsumption = Comsumption([])
			for i in range(0,Config.CONSUMPTION_COL):
				# Parse comsumption data
				for j in range(3,Config.CONSUMPTION_ROW):
					data = file.iloc[i,j]
					comsumption.appendComsumption(data)
					comsuptionsDataCount+=1
			self.comsumptions.append(comsumption)
			comsuptionsFileCount+=1
		# debug msg
		print("Comsumptions File load finish,total:{0}.".format(comsuptionsFileCount))
		print("Comsumptions data created,total:{0}.".format(comsuptionsDataCount))
		print("File loading process finish.")
	# Assigned random comsuption & generate amounts of user data
	"""def generateUsers(self,amount):
		print("Generating {0} users data...".format(amount+1))
		idx = 0
		while idx < amount+1:	
			self.users.append(self.generateUser(idx))
			idx+=1
		print("User data generation finished")
	"""	
	def generateUsers(self):
		print("Please enter amount of user data wants to generated")
		numOfUser = input ("Numbers -> ")
		self.totalNoUsers = int(numOfUser)
		print("Please enter persentage of user have PVs")
		persentage = input ("Persentage -> ")
		persentageInUse = float(persentage)/float(100.00)
		idx = 0
		while idx < int(self.totalNoUsers)+1:
			if(idx < int(self.totalNoUsers) * float(persentageInUse)):
				self.users.append(self.generateUser(idx,True))
				idx+=1
			else:
				self.users.append(self.generateUser(idx,False))
				idx+=1

	# Generating a user data
	def generateUser(self,userId,isHavePV):
		cFactor = random.gauss(Config.CMAXMEAN,Config.CMAXDEV)
		while (cFactor > Config.CMAXMAX or cFactor < Config.CMINMAX):
			cFactor = random.gauss(Config.CMAXMEAN,Config.CMAXDEV)
		# Calc PVFactor
		meanCapacityPV = (Config.MINCAPACITYPV + Config.MAXCAPACITYPV) / 2
		devCapacityPV = (Config.MAXCAPACITYPV - meanCapacityPV) / 3
		pvFactor = None
		pvFactor_t = random.gauss(meanCapacityPV,devCapacityPV)
		if(pvFactor_t < Config.MINCAPACITYPV):
			pvFactor = Config.MINCAPACITYPV
		elif(pvFactor_t > Config.MAXCAPACITYPV):
			pvFactor = Config.MAXCAPACITYPV
		else:
			pvFactor = pvFactor_t		
		if(isHavePV == True): 
			pv = self.photoVoltaics.getpvFactorizedPv(pvFactor)	
		else: 
			pv = self.photoVoltaics.getpvFactorizedPv(0)
		# print(pv[100].getProduction())
		# randomly assign Location
		location = self.locations.random()
		# new user object
		comsumption = self.comsumptions.random()

		user = User(userId,pvFactor,cFactor,pv,comsumption,location)
		# debug
		# print(comsumption.getComsumptions()[0])
		# print(len(user.getComsumptions()))
		
		
			
		return user
	
	# generate PV graph for a user
	def generateUserGraph(self,id,start_index,end_index):
		# id = 0
		user = self.users.getUser(id)
		pvs = user.getPv()
		comsumptions = user.getComsumptions()
		x = []
		y = []
		y2 = []
		y3 = []
		# time = []
		for i in range(start_index,end_index):
			#time.append(pvs[i].getTime())
			# date = pvs[i].getDate()
			production = pvs[i].getProduction()
			x.append(i)
			y.append(production)
			comsuption = comsumptions[i]
			y2.append(comsuption)
			feedin = user.getFeedin(pvs[i],comsuption)
			y3.append(feedin)

		chart.plot(x,y,color='blue')
		chart.plot(x,y2,color='red')
		chart.plot(x,y3,color='green')
		chart.xlabel("Time/15 Min")
		chart.ylabel("production PV(blue)comsuption(red)feedin(green)")
		chart.title('Userid: {0}'.format(id))
		# chart.xticks(x,time)
		chart.show()
		self.menu()
	# Generate Comsumption data for a user
	#def generateUserComsumption(self,start_index,end_index):
	#	id = 0
	#	user = self.users.getUser(id)
	#	comsumptions = user.getComsumptions()
	#	x = []
	#	y = []
	#	# time = []
	#	for i in range(start_index,end_index):
	#		#time.append(pvs[i].getTime())
	#		# date = pvs[i].getDate()
	#		comsuption = comsumptions[i]
	#		x.append(i)
	#		y.append(comsuption)
	#	
	#	chart.plot(x,y)
	#	chart.xlabel("Time/15 Min")
	#	chart.ylabel("comsuption C")
	#	# chart.xticks(x,time)
	#	chart.show()
	def debugPurchesAndFeedin(self):
		id = 0
		time = 5
		user = self.users.getUser(id)
		pv = user.getPvByIndex(time)
		c = user.getComsumptionByIndex(time)
		price = user.getPrice(time)
		feedIn = user.getFeedin(pv,c)
		purches = user.getPurchase(pv,c)
		print("Price: {0} Feedin: {1} purches: {2}".format(price,feedIn,purches))
	# debug pv
	def debugPV(self):
		print(self.photoVoltaics)

	def generateCSVRefenceFile(self):
		FileCSV.overwriteCsv()
		for i in range(0,35040):
			if(i%2 == 0): 
				for j in range(1,self.totalNoUsers):
					print("time idx = {0}".format(i))
					user = self.users.getUser(j)
					FileCSV.csv_feedin_purchase_1(user, i)
					# Packet.sendPacketHistory(user,timeIdx)


	def sendPacketByUserId(self,userId,timeIdx):
		print("time idx = {0}".format(timeIdx))
		user = self.users.getUser(userId)
		Packet.sendPacketHistory(user,timeIdx)
	# Send user data (ordered)
	def sendPacket(self):
		Packet.printServerInfo()
		for i in range(0,35040):
			for j in range(1,self.totalNoUsers):
				self.sendPacketByUserId(j,i)
	# Send user data (un ordered) by time intergral 
	# note the intergrals is minutes, default is 15
	def sendPacketByInterval(self,minutesIntergral):
		Packet.printServerInfo()
		generatedIdx = []
		# mins = datetime.datetime.now().strftime('%M')
		while True:
			minutes = datetime.datetime.now().strftime('%M')
			#second = datetime.datetime.now().strftime('%S')	
			if int(minutes) % minutesIntergral == 0:	
			#if int(second) % minutesIntergral == 0:
				for i in range(1,self.totalNoUsers):
					print(i)
					idx = random.choice(range(1,self.totalNoUsers))
					while idx in generatedIdx:
						idx = random.choice(range(1,self.totalNoUsers))
					generatedIdx.append(idx)
					self.sendPacketByUserId(idx, Utils.currentTimeToTimeIdx())
				generatedIdx.clear()
				time.sleep(60)
	# Send user data (un ordered)
	def sendPacketRamble(self):
		Packet.printServerInfo()
		generatedIdx = []
		for i in range(0,35040):
			if i == 35049:
				i = 0
			for j in range(1,self.totalNoUsers):
				idx = random.choice(range(1,self.totalNoUsers))
				while idx in generatedIdx:
					idx = random.choice(range(1,self.totalNoUsers))
				#print("user id {0}".format(idx))
				self.sendPacketByUserId(idx,Utils.currentTimeToTimeIdx())
				# Fix problem that i forgot to add current idx into the list.
				generatedIdx.append(idx)
				#time.sleep(0.1)
			generatedIdx.clear()
	def menu(self):
		mode = '0'
		while mode == '0':
			print("=====================")
			print("Simulator Program")
			print("HOST: " + Config.C_VAUE + "{0}".format(Config.HOST_ADDR) + Config.C_NORMAL)
			print("PORT: " + Config.C_VAUE + "{0}".format(Config.HOST_PORT) + Config.C_NORMAL)
			print("CLIENT_NAME: " + Config.C_VAUE + "{0}".format(Config.HOST_CLIENT) + Config.C_NORMAL)
			print("=====================")
			print("1.Send data by sequence (Ordered)")
			print("2.Send data by unsequenced (Un Ordered)")
			print("3.Send data by interval (15 Mins)")
			print("4.Display data chart")
			print("5.Generate CSV File")
			print("6.Exit Program")
			mode = input ("Selection -> ")
			if(mode == '1'):
				self.sendPacket()
			elif(mode == '2'):
				self.sendPacketRamble()
			elif(mode == '3'):
				minutes = 15
				self.sendPacketByInterval(minutes)
			elif(mode == '4'):
				userId = input ("Which user ? (please enter id) ->")
				timeIntergralstart = input ("time intergral start ? (please enter as interger number) ->")
				timeIntergralend = input ("time intergral end ? (please enter as interger number) ->")
				self.generateUserGraph(int(userId),int(timeIntergralstart),int(timeIntergralend))
				#self.generateUserComsumption(int(userId),int(timeIntergral))
			elif(mode == '5'):
				self.generateCSVRefenceFile()
			elif(mode == '6'):
				sys.exit()
				return
			else:
				print("Sorry, invaild option.")
				self.menu()
			
	def __init__(self):
		try:
			self.setup()
			# Graph
			#self.generateUserGraph(0,96)
			#self.generateUserComsumption(0,96)
			#self.debugPurchesAndFeedin()
			# Send data
			#self.sendPacket()
			#self.sendPacketByInterval(15)
			# Main Menu
			self.menu()
		except Exception as e:
			print("Sorry, an error has occur :( \n"+Config.C_VAUE+"{0}".format(e))
			self.menu()
			




