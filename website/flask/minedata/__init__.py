import flask
from flask import Flask, url_for, render_template, json, request, g
app = Flask(__name__, static_folder="static")
import views,models

print "loading Mine Data"
flask.g = {}
flask.g["mineData"] = models.mineMineData()
