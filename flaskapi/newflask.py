#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request #New-- can do lots of uses!
                            #reads data attached to incoming request from clients
                            #when a client posts somethin, request read that somthine
from flask import render_template #new-- takes an html and returns it


app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

@app.route("/")
def start():
    return render_template("postmaker.html") #flask is going to autotically search for a directory.

@app.route("/login",methods=["GET","POST"])
def something():
    #If a get was sent

    if request.method == "GET":
        return "You succesfully Getted!"
    elif request.method == "POST":
        if request.form["nm"]:

        return "You successfully POSTed!"
    return "You posted!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
