# This is a list
#states = ["Delaware", "Pennsylvania", "New York"]

# the [2] is the third object in the list or [-2] in reverse
#test = states[2]
#one = states[-2]
# changing new york to NY
#test1 = states[2] = "NY"

# below are list data types  to add to a list
#states.append("BLAHHH")
#print(states.count("Pennsylvania"))
#print(states)

#####################################################################################################
'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0])
vertical = int(position[1])

a = map[vertical - 1][horizonal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
'''
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Response = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
a = int(Response)
computerpicks = [rock, paper, scissors]

if a == 0:
    print(rock)
    print(random.choice(computerpicks))

elif a == 1:
    print(paper)
    print(random.choice(computerpicks))

elif a == 2:
    print(scissors)
    print(random.choice(computerpicks))

