#!/bin/bash/env python3

loginfail = 0

#open file

#Use  a with as to open a file and connections.

with open("keystone.common.wsgi", "r") as snork:
    #file objectsm like snork, can be looped over!
    # No need to convert them in a list or string

    for x in snork:
        if "- - - - -] Authorization failed" in x:
            loginfail +=1
            print(x.split()[-1])


print("Number of failed authentications:", loginfail)
