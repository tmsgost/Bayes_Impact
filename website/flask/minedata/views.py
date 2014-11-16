from minedata import app
from flask import Flask, url_for, render_template, json, request
import models

@app.route("/")
def index():
	#url_for('static', filename='maps.js')
	return render_template('index.html',coords=models.parseCoords())

@app.route("/mines/", methods=['GET'])
def mines():
	if request.method == 'GET':
		return "here's the mine entry"


@app.route("/mines/<int:mineID>", methods=['GET'])
def mine(mineID):
	if request.method == 'GET':
		return "data for mine:" + str(mineID)
