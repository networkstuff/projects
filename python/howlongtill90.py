### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: how long till 90 years old

age = input("what is your current age: ")

a = 90 - int(age)

days = round(a * 365)
weeks = round(a * 52)
months = round(a * 12)

print(f"you have {days} days, {weeks} weeks, and {months} months left")