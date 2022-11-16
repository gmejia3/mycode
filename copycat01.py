#!/usr/bin/env python3

#The following code shows how we can use shutil and os to make copies of files and directories.

#import additional code to complete our task
import shutil
import os

#This code allows the user to run the program from any location on the system, and our script still always start at /home/student/mycode/
# move into the working directory.
os.chdir("/home/student/mycode/")

# copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")


