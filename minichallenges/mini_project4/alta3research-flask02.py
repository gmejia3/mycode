#!/usr/bin/env python3

import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/"



new_issue= [{
    "Google The Answer": "We have technology! Use it's inifinte wisdom!"
              
             }]

new_issue = json.dumps(new_issue)

resp = requests.post(URL, json = new_issue)



#@app.route("/present", methods=["GET","POST"])
#def index():
#    if request.method == 'POST':
#        data = request.json
#        if data:
#           data= json.loads(data)
#           name = data["name"]
#           realName = data["realName"]
#           since = data["since"]
#           powers = data["powers"]
#           herodata.append({"name":name,"realName":realName,"since":since,"powers":powers})

 #   return jsonify(herodata)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=2224)
