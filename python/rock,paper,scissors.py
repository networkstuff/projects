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

Response = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n ")
a = int(Response)
images = [rock, paper, scissors]
computerselected = random.randint(0, 2)

if a >= 3:
    print("You typed an invalid number, you lose!")
    exit(50)

elif a == 0:
    print(rock)
    print(images[computerselected])

    if computerselected == 1 and a == 0:
        print(" you lose")
        exit(300)

    elif computerselected == 2 and a == 0:
        print("you win")
        exit(400)

    else:
        print("tie")
        exit(500)

elif a == 1:
    print(paper)
    print(images[computerselected])

    if computerselected == 2 and a == 1:
        print("you lose")
        exit(300)
    elif computerselected == 0 and a == 1:
        print("you win")
        exit(400)
    else:
        print("tie")
        exit(500)

elif a == 2:
    print(scissors)
    print(images[computerselected])

    if computerselected == 0 and a == 2:
        print(" you lose")
        exit(300)

    elif computerselected == 1 and a == 2:
        print("you win")
        exit(400)
    else:
        print("tie")
        exit(500)
