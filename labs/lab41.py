#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Starlord, Mystiqu, Hulk) \n>")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) \n>")

marvelchars= {
                "Starlord":
                {"real name": "peter quill",
                "powers": "dance moves",
                "archenemy": "Thanos"},

                "Mystique":
                {"real name": "raven darkholme",
                "powers": "shape shifter",
                "archenemy": "Professor X"},

                "Hulk":
                 {"real name": "bruce banner",
                "powers": "super strength",
                "archenemy": "adrenaline"}    
             }

name = char_name
stat = char_stat
value = marvelchars[char_name][char_stat] 

print(f"{name}'s {stat} is: {value}")
