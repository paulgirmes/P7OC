import json
from flask import Flask
from flask import url_for
from app.models.search_request import Request
from . import config

app = Flask(__name__)
from flask import request
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    key = {"key": config.Config.google_api}
    return render_template("index.html", title="home", key=key)


@app.route("/question", methods=["POST"])
def question():
    answer = Request(request.form["text"])
    try:
        return json.dumps(answer.process())
    except Exception as e:
        return json.dumps(
            {
                "status": "NOK",
                "adresses_answer": "OUPS ! , un Problème est survenu dans le traitement des données : "+ e.__traceback__
            }
        )
