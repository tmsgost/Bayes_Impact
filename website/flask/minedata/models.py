import csv
import flask
from flask import g

#DATASET="minedata/data"
DATASET="/opt/minedataset"

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

def mineAccidentData():
	# 100MB file size limit for github, so just splitting into 2 for now...
	accidentData = []

	fin = open( DATASET + '/Accidents.txt','r' )
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		accidentData.append(row)

	"""
	fin = open( DATASET + '/Accidents.txt.1','r' )
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		accidentData.append(row)

	fin = open( DATASET + '/Accidents.txt.2','r' )
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		accidentData.append(row)
	"""

	return accidentData

# currently only reading in violation data for 2013 as dataset is too large...
def mineViolationData():
	#fin = open( DATASET + '/Violations.txt','r' )
	fin = open( DATASET + '/Violations.2013','r' )
	violationData = []
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		violationData.append(row)

	return violationData

# get all violation scores (for now)
def getViolationScores():
	return flask.g["violationScores"]

# returns all the mines
def getMines():
	return flask.g["mineData"]

# returns all accidents
def getAccidents():
	return flask.g["accidentData"]

# returns all violations
def getViolations():
	return flask.g["violationData"]

# returns all the accidents for a given year range (inclusive)
def getAccidentsForRange(startYear,endYear):
	accidentList = []
	for accident in getAccidents():
		try:
			if int(accident["CAL_YR"]) >= int(startYear) and int(accident["CAL_YR"]) <= int(endYear):
				accidentList.append(accident)
		except:
			pass

	return accidentList

# returns all the violations for a given year range (inclusive)
def getViolationsForRange(startYear,endYear):
	violationList = []
	for violation in getViolations():
		try:
			if int(violation["CAL_YR"]) >= int(startYear) and int(violation["CAL_YR"]) <= int(endYear):
				violationList.append(violation)
		except:
			pass

	return violationList

# returns all accidents resulting in a fatality, given a list of accidents
def getFatalAccidents(accidentList):
	fatalityList = []
	for accident in accidentList:
		try:
			if accident["DEGREE_INJURY"] == "FATALITY":
				fatalityList.append(accident)
		except:
			pass

	return fatalityList

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
