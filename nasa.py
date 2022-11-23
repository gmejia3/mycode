#!/usr/bin/env python3

import pprint
import requests

URL ='https://api.nasa.gov/planetary/apod?api_key=5iX0XHISdwzwWc7oq4cI7viQHdqiPPvSfYJxXsn4'

input = (What date do you want to see a picture?)

response = requests.get(URL + "&start_date=2022-11-18&end_date=2022-11-22").json()
pprint.pprint(response)



