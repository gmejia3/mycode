#!/usr/bin/env python3

import newquestions
import time
import os


possible_results = {
                        "A": ["Brontosaurus", "The Giver"],
                        "B": ["Pterodactyl", "The Supervisor"],
                        "C": ["Triceratops", "The Mastermind "],
                        "D": ["T-Rex", "The Idealist "],
                        "E": ["Stegosaurus ", "The Visionary "]
                    }

nugget = "PLACEHOLDER"
personality = "PLACEHOLDER"

def process_answer(quiz_answer):
    if quiz_answer == "A":
        nugget = possible_results["A"][0]
        personality = possible_results["A"][1]
    elif quiz_answer == "B":
        nugget = possible_results["B"][0]
        personality = possible_results["B"][1] 
    elif quiz_answer == "C":
        nugget = possible_results["C"][0]
        personality = possible_results["C"][1] 
    elif quiz_answer == "D":
        nugget = possible_results["D"][0]
        personality = possible_results["D"][1] 
    elif quiz_answer == "E":
        nugget = possible_results["E"][0]
        personality = possible_results["E"][1] 

    return nugget, personality    

def main():

    print("Watch Us Guess Your Dino Buddy Shape And Reveal Your Personality!")
    time.sleep(1)  #Pause for dramaticness
    os.system('clear') #Clear Screen?
    
    # Quiz directions  
    print("We will ask you a series of questions. \n Please respond with a-e.")

    newquestions.questionaction()
    final_answer = newquestions.questionaction()
    process_answer(final_answer)
    what = process_answer(final_answer) 
    
    time.sleep(1)

    # results reveal 
    os.system('clear')
    
    print("Congrats! You survived the quiz!")
    time.sleep(1)
    #os.system('clear')
    print("\nPlease wait while we calculate your results.")
    time.sleep(5)

    os.system('clear')
    print("Drum Roll please\n\n")
    time.sleep(2)
    print(f"your favorite chicken nugget shape is! \n\n-------------->   {what[0]}   <--------------\n\n")
    time.sleep(2)
    print("More Drums please\n\n")
    time.sleep(2)
    print(f"Your personality is! \n\n-------------->   {what[1]}   <---------------\n\n\n\n\n")
    time.sleep(2)
    print("Thank you for giving us your precious time!\n\n\n\n\n")  

main()
