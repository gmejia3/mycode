#!/usr/bin/env python3

from flask import Flask


#Flask make me an APP

app= Flask(__name__)

@app.route("/pickachu")          # <----- Decorator
def helloword():
    return {"name" :"Pika pika!",
            "type" : "electrctir",
            "generation": 1}

@app.route("/bulbasaur")
def red():
    return {"name" :"Leafs!",
            "type" : "grass",
            "generation": 1}



app.run(host="0.0.0.0", port=2224)
