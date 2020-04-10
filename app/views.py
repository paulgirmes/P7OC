import json
from flask import request
from flask import render_template
from app import app
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
    if answer.process() == 0:
        return json.dumps({'status':'OK','answer':answer.adress, 'lng':answer.coordinates['lng'], 'lat':answer.coordinates['lat']})
    else:
        return json.dumps({'status':'NOK','answer':"précise ta question"})