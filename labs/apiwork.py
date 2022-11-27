#!/usr/bin/env python3

# METHOD 1
# Standard library

import json
import urllib.request

URL = "https://thesimpsonsquoteapi.glitch.me/quotes"

#Send a get request

httpresponse = urllib.request.urlopen(URL)

data = httpresponse.read()

gooddata = data.decode("utf-8")

finallypython= json.loads(gooddata)

print(finallypython[0]["quote"])
print("       --", finallypython[0]["character"])
