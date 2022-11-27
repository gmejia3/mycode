#!/usr/bin/env python3



farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]

for x in NE_animals:
    print(x)

user_answer = input("Choose a farm to pick from animals: NE Farm, W Farm, SE Farm")

user_animals = farms["user_answer"]["agriculture"]

for x in user_animals:
    print(x)
