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
	fin = open( DATASET + '/Mines.txt','r' )
	mineData = []
	reader = csv.DictReader(fin, delimiter="|", quotechar='"')
	for row in reader:
		mineData.append(row)

	return mineData

# retruns all the mines
def getMines():
	return flask.g["mineData"]
	
def getMine(mineID):
	#mineData = mineMineData()
	#return str(mineID)
	
	try:
		
		for mine in flask.g["mineData"]:
			if int(mine["MINE_ID"]) == int(mineID):
				print "FOUND"
				return mine
	except:
		return None


# returns a json blob of all the coordinates of all mines in the US
def getMineCoords():
	coords = []
	for mine in flask.g["mineData"]:
		if mine["LATITUDE"] != "" and mine["LONGITUDE"] != "":
			coord = [mine["MINE_ID"], mine["LATITUDE"], mine["LONGITUDE"]]
			coords.append(coord)
	return coords
