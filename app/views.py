import json
from flask import Flask
app = Flask(__name__)
from flask import request
from flask import render_template
from app.utils.utils import Request
from . import config
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
@app.route("/")
@app.route("/index")
def index():
    coordonees = {"lat": "48.8747265", "long": "2.3505517"}
    key = {"key" : config.Config.google_api}
    position ={"lat": coordonees.get("lat"), "long": coordonees.get("long")}
    return render_template("index.html", title="home", key=key, position=position)

@app.route('/question', methods=['POST'])
def question():
    answer = Request(request.form['text'])
    try:
        return json.dumps(answer.process())
    except:
        return json.dumps({'status':'NOK','adresses_answer':"Problème dans le traitement des données"})