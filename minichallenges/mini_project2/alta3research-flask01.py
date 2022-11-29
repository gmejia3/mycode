#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
import options

#Make an application called app with Flask

app = Flask(__name__)

#Homepage of the game and goes to the index.html
@app.route("/")
@app.route("/start")
def homepage():
    return render_template("index.html") 

@app.route("/options")
def options():
    return render_template("selections.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) #Runs the application on local machine
