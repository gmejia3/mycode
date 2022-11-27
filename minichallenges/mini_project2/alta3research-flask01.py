#!/usr/bin/env python3

from flask import Flask, redirect, url_for, request, render_template

#Make an application called app with Flask

app = Flask(__name__)

#Homepage of the game and goes to the index.html
@app.route("/")
def homepage():
    return render_template("index.html")












if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) #Runs the application on local machine
