from minedata import app
from flask import Flask, url_for, render_template, json, request
import models

@app.route("/")
def index():
	#url_for('static', filename='maps.js')
	return render_template('index.html',coords=models.parseCoords())

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
	#return models.getMineCoords()
	return json.dumps(models.getMineCoords())