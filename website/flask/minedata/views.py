from minedata import app
from flask import Flask, url_for, render_template, json, request
import models

@app.route("/")
def index():
	
	# ALL MINES
	mines = models.getMines()
	coords = models.getMineCoords(mines)

	# MINES WITH VIOLATION SCORE >= 6000
	#coords = models.getMineCoords( models.getMinesByViolationScore("6000") )
	
	return render_template('index.html',coords=coords)

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

# show mines more dangerous than threshold
@app.route("/mines/scores/<int:violationScoreThreshold>", methods=['GET'])
def violationScoreQuery(violationScoreThreshold):
	if request.method == 'GET':
		
		# restrict threshold
		if violationScoreThreshold < 1000:
			return "Threshold too small"

		return json.dumps( models.getMinesByViolationScore(violationScoreThreshold) )
