#!/usr/bin/env python3

#Create a list constaining network information
my_list = ["192.168.0.5", 5060, "UP"]

#Print out the IP Address
print(f"The first item in the list (IP): {my_list[0]}")

#Print out the Port
print(f"The second item in the list (port): {str(my_list[1])}")

#Print out the state
print(f"The third item in the list (state): {my_list[2]}")

print(my_list[0])

iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print(iplist[3:5])
