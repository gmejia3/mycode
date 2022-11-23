#!/usr/bin/enc python3

#Used to make API requests much eaiser.
import requests
import datetime

URL = 'http://api.open-notify.org/iss-now.json'

def main():

    #Get request to webserver
    apicall = requests.get(URL).json()
    
    #Save results to variables.
    latitude = apicall["iss_position"]["latitude"]
    longitude = apicall["iss_position"]["longitude"]
    timeget = apicall["timestamp"]
    
    #Use datetime to convert from epoch to datetime.
    timeanswer = datetime.datetime.fromtimestamp(timeget).strftime('%Y-%m-%d %H:%M:%S')

    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {timeanswer}\nLon: {longitude}\nLat: {latitude}")
    






















if __name__ == "__main__":
    main()
