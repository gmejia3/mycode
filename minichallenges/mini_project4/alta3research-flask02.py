#!/usr/bin/env python3

import requests
import json
from pprint import pprint

#URL = "http://127.0.0.1:2224/"
URL = "https://aux1-3ad56d70-b523-46d0-93d7-fabc0204e67a.live.alta3.com/testing"



new_issue= [{
    "Google The Answer": "We have technology! Use it's inifinte wisdom!"
              
             }]

new_issue = json.dumps(new_issue)

resp = requests.get(URL).json()
print(resp)



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
