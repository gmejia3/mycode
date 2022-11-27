#!/usr/bin/env python3

import html
import time

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

print("Welcome to trivia question!")
time.sleep(2)
ready = input("Are you ready for your single question?")

if ready != "yes": 
    end()
elif ready == "yes":
    pass


print(trivia["question"])

time.sleep(2)

a = html.unescape(trivia["incorrect_answers"][1])
b = html.unescape(trivia["correct_answer"])
c = html.unescape(trivia["incorrect_answers"][2])
d = html.unescape(trivia["incorrect_answers"][0])

print(f"\n{a}\n{b}\n{c}\n{d}")
