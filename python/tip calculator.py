### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: tip calculator


number1 = 10
number2 = 12
number3 = 15

print("welcome to the tip calculator!.")
two = (float(input("what was the total bill? ")))
three = float(input(f"what percentage tip would you to give? {number1}, {number2}, or {number3}? "))
four = int(input("How many people to split the bill? "))
h = (round(int((two / four)))) * three
d = "{:.2f}".format(h)
print(f"each person should pay: {d} ")

#################OR###################################

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)