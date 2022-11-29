#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

#Constructor for Flask application
app = Flask(__name__)

limiter = Limiter(app,key_func = get_remote_address,
        default_limits = ["100 per day", "30 per hour"])

#limiter decorator to limit the requests for this function.
@app.route("/success/<name>")
@limiter.limit("10 per day")
def success(name):
    #if "past" in request.form:
#    if request.form.get('past') == 'Past':
#        return render_template("past.html")
    #    return redirect(url_for("past"))
    #elif "present" in request.form:
#    elif request.form.get('present') == 'Present':
#        return render_template("present.html")
    #    return redirect(url_for("present"))
    return render_template("success.html", name = name)

#def options():
  #  if request.form.get('past') == 'Past':
  #      return redirect(url_for("past"))
  #  elif request.form.get('present') == 'Present':
  #      return redirect(url_for("present"))

@app.route("/past")
def past():
    return render_template("past.html")

@app.route("/present")
def present():
    return render_template("present.html")

# This is the starting point for the users. Either / or /start.
@app.route("/") 
@app.route("/start") 
@limiter.limit("5 per day")
def start():
    return render_template("postmaker.html") 

# login for user to either POST or GET.
@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get("nm"): 
            user = request.form.get("nm") 
        else: 
            user = "defaultuser"
    
    elif request.method == "GET":
        if request.args.get("nm"): 
            user = request.args.get("nm") 
        else:
            #if no username is submitted.
            user = "defaultuser" 
    return redirect(url_for("success", name = user)) # pass back to /success with val for name







if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

