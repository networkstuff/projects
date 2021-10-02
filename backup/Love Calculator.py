### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: calculates love compatibility

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_case = combined_names.lower()

true = lower_case.count('t') + lower_case.count('r') + lower_case.count('u') + lower_case.count('e')
love = lower_case.count('l') + lower_case.count('o') + lower_case.count('v') + lower_case.count('e')

total_amount = int(str(true) + str(love))

if (total_amount < 10) or (total_amount > 90):
    print(f"Your score is {total_amount}%, you go together like coke and mentos.")

elif (total_amount >= 40) and (total_amount <= 50):
    print(f"Your score is {total_amount}%, you are alright together.")

else:
    print(f"Your score is {total_amount}%.")
