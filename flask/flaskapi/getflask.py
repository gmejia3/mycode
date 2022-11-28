#!/usr/bin/env python3

import requests

URL = "https://aux1-3ad56d70-b523-46d0-93d7-fabc0204e67a.live.alta3.com/endpoint1"

response = requests.get(URL).json()

print(response)


