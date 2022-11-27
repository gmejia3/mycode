#!/usr/bin/python3
"""Reviewing how to parse json"""

#JSON is part of the Python Standard Libaray
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeudian"},
            {"name": "Arthur Dent", "Species": "Human"}]

    ##Display our Python Data (A list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode
    with open("galaxyguide.json", "w") as zfile:
        ## use the JSON Library
        ## USAGE: Json.dump(input data, file like object) ##
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()

