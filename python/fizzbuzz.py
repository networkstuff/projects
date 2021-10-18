### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: The challenge is to check if the number from 1 to 100 divided by a number (3 or 5) is equal or not. 
#if the number is equal (meaning no left over) than it will print fizbuzz, fizz or buzz depending on the outcome.
# if all is false than the outcome is the number is printed meaning the number divided by 3 or 5 is not an even number.

for number in range(1, 101):

    if (number % 3) == 0 and number % 5 == 0:
        print(f"fizzbuzz")
    elif (number % 3) == 0:
        print(f"fizz")
    elif (number % 5) == 0:
        print(f"buzz")
    else:
        print(number)
