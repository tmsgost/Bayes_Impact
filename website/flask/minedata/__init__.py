import flask
from flask import Flask, url_for, render_template, json, request, g
app = Flask(__name__, static_folder="static")
import views,models

print "loading Mine Data"
flask.g = {}
flask.g["mineData"] = models.mineMineData()
flask.g["activeMineData"] = models.mineActiveMineData()

print "loading Violation Score Data"
flask.g["violationScores"] = models.mineViolationScores()

print "loading Accident Data"
flask.g["accidentData"] = models.mineAccidentData()

print "loading Violation Data (2013 ONLY for now!!!)"
flask.g["violationData"] = models.mineViolationData()

# load in risk scores & update mine data
print "loading lives at risk scores"
flask.g["mineLivesAtRisk"] = models.mineLivesAtRisk()
