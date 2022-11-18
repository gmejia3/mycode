#!/usr/bin/env python3

import re
import statistics

def question1():
   
    while True:
        print("\nChoose a cat emotion")
        answer1 = input("\nA. Happy \nB. Sad \nC. Hungry \nD. Angry \nE. I'm not sure\n>").capitalize()
        if answer1 == "A" or answer1 == "B" or answer1 == "C" or answer1 == "D" or answer1 == "E":
            return answer1
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question2():
    while True:
        print("\nChoose a veggie")
        answer2 = input("\nA. Artichoke \nB. Kale  \nC. Peas \nD. Bok Choy \nE. I'm not sure\n>").capitalize()
        if answer2 == "A" or answer2 == "B" or answer2 == "C" or answer2 == "D" or answer2 == "E":
            return answer2
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question3():
    while True:
        print("\nChoose a console")
        answer3 = input("\nA. Switch \nB. PlayStation \nC. Xbox \nD. SuperComputer \nE. I'm not sure\n>").capitalize()
        if answer3 == "A" or answer3 == "B" or answer3 == "C" or answer3 == "D" or answer3 == "E":
            return answer3
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question4():
    while True:
        print("\nChoose a stuffed animal")
        answer4 = input("\nA. Teddybear \nB. Cat \nC. Dog \nD. Peacock \nE. I'm not sure\n>").capitalize()
        if answer4 == "A" or answer4 == "B" or answer4 == "C" or answer4 == "D" or answer4 == "E":
            return answer4
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question5():
    while True:
        print("\nChoose a snack")
        answer5 = input("\nA. Hot Cheetos \nB. Popcorn \nC. Mixed Nuts \nD. Seaweed \nE. I'm not sure\n>").capitalize()
        if answer5 == "A" or answer5 == "B" or answer5 == "C" or answer5 == "D" or answer5 == "E":
            return answer5
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question6():
    while True:
        print("\nPick a color")
        answer6 = input("\nA. Red \nB. Blue \nC. Yellow \nD. Green \nE. I'm not sure\n>").capitalize()
        if answer6 == "A" or answer6 == "B" or answer6 == "C" or answer6 == "D" or answer6 == "E":
            return answer6
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def question7():
    while True:
        print("\nWhats your favorite holiday?")
        answer7 = input("\nA. Christmas \nB. Thanksgiving \nC. Veterans Day \nD. Leif Erickson Day \nE. I'm not sure\n>").capitalize()
        if answer7 == "A" or answer7 == "B" or answer7 == "C" or answer7 == "D" or answer7 == "E":
            return answer7
            break
        else:
            print("Sorry you did not enter a, b, c, d, e,")
            continue

def questionaction():
    result_list = []
    condition = 0
    while condition == 0:
        
        result_list.append(question1())
        result_list.append(question2())
        result_list.append(question3())
        result_list.append(question4())
        result_list.append(question5())
        result_list.append(question6())
        result_list.append(question7())
        results = statistics.mode(result_list)

        condition += 1

    return results
def main():
    print("\n")

main()


if __name__ ==" __main__":
    main()

