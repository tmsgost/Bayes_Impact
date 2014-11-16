import csv
import flask
from flask import g

DATASET="minedata/data"

def parseCoords():
	fin = open( DATASET + '/Mines.head','r' )
	fin.readline() # throw away header
	coords = []
	for line in fin:
		mineID = line.split('|')[0].replace('"','')
		latitude = line.split('|')[44].replace('"','')
		longitude = line.split('|')[43].replace('"','')
		
		coord = [mineID, latitude, "-"+longitude]
		coords.append(coord)
	return coords

# loads mine data into memory
def mineMineData():
	# load base mine data
	fin = open( DATASET + '/Mines.txt','r' )
	mineData = []
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		mineData.append(row)

	return mineData

def mineViolationScores():
	# load violation scores
	fin = open( DATASET + '/violationscore.csv','r' )
	violationScores = []
	reader = csv.DictReader(fin, delimiter=",")
	for row in reader:
		violationScores.append(row)
	return violationScores

# get all violation scores (for now)
def getViolationScores():
	return flask.g["violationScores"]

# returns all the mines
def getMines():
	return flask.g["mineData"]

def getActiveMines():
	mineList = []
	for mine in getMines():
		if mine["CURRENT_MINE_STATUS"] == "Active":
			mineList.append(mine)
	return mineList

def getMine(mineID):
	try:
		for mine in flask.g["mineData"]:
			if int(mine["MINE_ID"]) == int(mineID):
				return mine
	except:
		return None

# given a list of mines (entire mine objects), return the coordinates in form:
# MINE_ID, LATITUDE, LONGITUDE, CURRENT_MINE_NAME
def getMineCoords(mineList):
	coords = []
	#for mine in flask.g["mineData"]:
	for mine in mineList:
		if mine["LATITUDE"] != "" and mine["LONGITUDE"] != "":
			coord = [mine["MINE_ID"], mine["LATITUDE"], "-"+mine["LONGITUDE"], mine["CURRENT_MINE_NAME"]]
			coords.append(coord)
	return coords

# returns a list of mines equal to or greater than a threshold
def getMinesByViolationScore(violationScore):
	mineList = []
	for mine in flask.g["violationScores"]:
		try:
			if float(mine["score"]) >= int(violationScore):
				mineList.append( getMine(mine["MINE_ID"]) )
		except:
			pass

	return mineList
