#!/usr/bin/env python3

import requests

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"

#send a get request.
httprespone = requests.get(URL)
        #.put()
        #.delete()
        #.post()

data= httprespone.json()

print(data[0]["quote"])

