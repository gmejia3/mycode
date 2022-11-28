#!/usr/bin/env python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
#variable "app" represents our entire api!
#This whole script is "teaching" our little app object how to behave?
app = Flask(__name__) # __name__ == name of the module we're current running

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/Giovanni")         #Decorator
def hello_world():
    return {'boolean': True, "value": None}

@app.route("/endpoint1")
def next_endpoint():
    return {
            "name": "student", 
            "passion": "stepping on programming rakes", 
            "More to learn": True
            }

@app.route("/endpoint2")
def another_endpoint():
    return { 
            "name": "student", 
            "passion": "stepping on programming rakes", 
            "More to practice": True
            }

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

