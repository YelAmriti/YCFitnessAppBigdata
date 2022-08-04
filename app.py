from flask import Flask
from flask_cors import CORS, cross_origin

import Felix
import Wouter
import VoortgangVisualisatie
import RunTipsScraping

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!!</p>"

@app.route("/tweede")
def Felixfunctie():
    return Felix.vanFelix1()

#return basic columns of csv
@app.route("/csv")
def csv():
    return Wouter.csvFunctie()

#return basic columns met stijl
@app.route("/csvMetStijl")
def csvStijl():
    return Wouter.csvStijl()

#return basic colomns in json format
@app.route("/csvJSON")
@cross_origin()
def csvJSON():
    return Wouter.csvJSON()

#return met input van adress
@app.route("/csv/<pok>")
def printpok(pok):
    return Wouter.printPokemon(pok)

#return vanaf api
@app.route("/apiCall")
def callapi():
    return Wouter.ApiCall()

#return vanaf api
@app.route("/apiWeer")
def printweer():
    return Wouter.NCdata()

#connectie met database en voortgang van route visualiseren
@app.route("/VoortgangVisual")
def printGraph():
    return VoortgangVisualisatie.ShowGraph()

#data scrapen van website en random tip tonen
@app.route("/RunTip")
def printRunTip():
    return RunTipsScraping.GetTip()


<<<<<<< HEAD
#voor niet flask refreshen, run python app.py met hieronder niet in commentaar
#app.run(debug=True)
=======
app.run(debug=True)
>>>>>>> main
