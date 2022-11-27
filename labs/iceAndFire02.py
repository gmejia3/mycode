#!/usr/bin/env python3

#Code gotta do the following:

#ask a user for a character

#Build a url that access that particular charater

#documentation for this API is at
# https://anapioficeandfire.com/Documentation

# x = list of book urls
# y = list of allegiances
# z = list of povbooks urls

#loop over that list of book urls and send a get request to each URL
#Grab the Json and pull out the name of the book and print it out.

import requests
import pprint

URL = "https://www.anapioficeandfire.com/api"

def main():

    ##send HTTPS GET to the API of ICE and Fire book resource
    gotresponse = requests.get(URL).json()

    ## Print the request with Pretty Print
    pprint.pprint(gotresponse)

    


if __name__ == "__main__":
    main()



















