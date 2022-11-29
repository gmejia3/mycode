#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

#Constructor for Flask application
app = Flask(__name__)

limiter = Limiter(app,key_func = get_remote_address,
        default_limits = ["100 per day", "30 per hour"])


coding_mistakes= [{
    "Mispelled Variable": "When working in Java lab, I mispelled a String variable so well that I could not find the mistake in my code because everything looked and operated correctly, except what I wanted to happen.",
    "Type Python Correctly": "Sometimes you are on a roll with checking your code that you cannot spell Python correctly. pyothn, pytohn, pythong, ptyhon, and any other combination will not work. Trust me, I did not mean to try.",
    "Check The Momentum": "If you are having the best day of your life and writing amazing code as if you are, Leonardo Di Ser Piero Da Vinci, take some time to test your code. If not you are going to remember thinking it was the best day of your life.",
    "Git Git Git": "You never know when your overzealous system admin is going to wipe everything. Do yourself a favor Queen/King, Commit and Push your life!",
    "Less/Greater will work": "Ever wonder why your index loop is not working? ***Hint*** It's problably because it never starded.",
    "Get Some Fresh Eyes!": "You can stare at your code all you want. You are not going to see the error unless its the Kool-Aid Man breaking through the wall kind of obvious. Have someone else take a quick look."}]


#limiter decorator to limit the requests for this function.
@app.route("/success/<name>")
@limiter.limit("10 per day")
def success(name):
    return render_template("success.html", name = name)

@app.route("/testing")
def testing():
    return jsonify(coding_mistakes)

@app.route("/past")
def past():
    return render_template("past.html", dictionary = coding_mistakes)

@app.route("/present", methods = ["POST", "GET"])
def present():
    if request.method == "POST":
        if request.form.get('mistake_name'):
            mistake_name = request.form['mistake_name']              #Mistake Name
            coding_mistakes.append(mistake_name)
        if request.form.get('mistake_description'):
            mistake_description = request.form['mistake_description']    #Mistake Description
            coding_mistakes.append(mistake_description)
            return render_template("past.html") # pass back to /success with val for name
    elif request.method == "GET":
        return render_template("present.html")

# This is the starting point for the users.
@app.route("/") 
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
            user = "I am too good to put in a name"
    
    elif request.method == "GET":
        if request.args.get("nm"): 
            user = request.args.get("nm") 
        else:
            #if no username is submitted.
            user = "I am too good to put in a name" 
    return redirect(url_for("success", name = user)) # pass back to /success with val for name


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

