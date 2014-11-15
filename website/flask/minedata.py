from flask import Flask, url_for, render_template, json

app = Flask(__name__)

DATASET="/Users/cdorros/Documents/Hackathons/BayesImpact/MineDataSets-local"

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

@app.route("/")
def index():
	#url_for('static', filename='maps.js')
	print json.dumps(parseCoords())
	return render_template('index.html',coords=parseCoords())

if __name__ == "__main__":
	app.run()
