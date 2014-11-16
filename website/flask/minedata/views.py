from minedata import app
from flask import Flask, url_for, render_template, json, request
import models

@app.route("/")
def index():
	
	# ALL MINES
	#mines = models.getMines()

	# ACTIVE MINES
	mines = models.getActiveMines()
        numMines = len(mines)

	# MINES WITH VIOLATION SCORE >= 6000
	#mines = models.getMinesByViolationScore("6000")

	numFatalities2013 = len(models.getFatalAccidents(
			models.getAccidentsForRange(2013,2013) ))

	numViolations2013 = len(models.getViolationsForRange(2013,2013))

	#fout = open(writemodels.getViolations(models.getViolationsForRange(2013,2013)

	coords = models.getMineCoords(mines)
	return render_template('index.html',coords=coords, numMines=numMines,
		numFatalities=numFatalities2013, numViolations=numViolations2013)

@app.route("/about/")
def about():
	return render_template('about.html')

@app.route("/analysis/")
def analysis():
	return render_template('analysis.html')

@app.route("/mines/")
def mines():
        # TODO - drop in mines
	mines = models.getActiveMines()
	return render_template('mines.html', mines=mines)

"""
utf8 errors - need to fix later...
@app.route("/mines/", methods=['GET'])
def mines():
	if request.method == 'GET':
		
		output = ""
		for mine in models.getMines():
			output = output + json.dumps(mine, ensure_ascii=False)
		return str(output)
		
		return json.dumps( models.getMines(), ensure_ascii=False)
"""

@app.route("/mines/<int:mineID>", methods=['GET'])
def mine(mineID):
	if request.method == 'GET':
		mine = models.getMine(mineID)
		if mine is None:
			return "Mine not found"
		else:
			return json.dumps(mine)

@app.route("/mines/coords", methods=['GET'])
def mineCoords():
	return json.dumps(models.getMineCoords())

@app.route("/mines/scores", methods=['GET'])
def violationScores():
	return json.dumps(models.getViolationScores())

# print list of accidents for one year
@app.route("/accidents/<int:year>", methods=['GET'])
def accidentsByYear(year):
	return json.dumps(models.getFatalAccidents(
			models.getAccidentsForRange(year,year) ))

# print list of violations for one year
@app.route("/violations/<int:year>", methods=['GET'])
def violationsByYear(year):
	# only 2013 for now since dataset is too large
	if int(year) != 2013:
		return "Only 2013 violation data is available"
	return json.dumps(models.getViolationsForRange(int(year),int(year)))

# show mines more dangerous than threshold
@app.route("/mines/scores/<int:violationScoreThreshold>", methods=['GET'])
def violationScoreQuery(violationScoreThreshold):
	if request.method == 'GET':
		
		# restrict threshold
		if violationScoreThreshold < 1000:
			return "Threshold too small"

		return json.dumps( models.getMinesByViolationScore(violationScoreThreshold) )
