#!/usr/bin/env python3

counter = 0

while True:
    counter += 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ").lower() #To fix the casing issue.
    if answer == 'brian':
        print('Correct')
        break # end the game
    elif answer == 'shrubbery':
        print("You gave the super secret answer!")
        break
    elif counter == 3:
        print("Sorry, the answer was Brian.")
        break # this will aslo end the game
    else:
        print("Sorry! Try again!")




