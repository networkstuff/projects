### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: randomization on who will pay for the meal today

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


b = random.randint(0, 4)

d = names[0]
e = names[1]
f = names[2]
g = names[3]
h = names[4]


if b == 0:
    print(f"{d} is going to buy the meal today!")

if b == 1:
    print(f"{e} is going to buy the meal today!")

if b == 2:
    print(f"{f} is going to buy the meal today!")

if b == 3:
    print(f"{g} is going to buy the meal today!")

if b == 4:
    print(f"{h} is going to buy the meal today!")

######################### or for a dynamic solution ###########################

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = len(names)
b = random.randint(0, a - 1)

c = names[b]

print(f"{c} is going to buy the meal today!")
