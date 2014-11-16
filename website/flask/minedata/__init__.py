from flask import Flask, url_for, render_template, json, request
app = Flask(__name__, static_folder="static")

import views,models
