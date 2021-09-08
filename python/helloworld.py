### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: Print, strings and its rules


## Normal print with double qoutes in the string allow to write whatever without it being taken as an expression
print("hello, world!")
## Normal print with different operators to add 2 values together
print(1 + 2)
print(7 * 6)
## Normal print with empty value equaling to emptey making space inbetween
print()
## Normal print with double qoutes for each vlue of its own generating space inbetween them
print("file", " file1?", "file2!", 3)
## same print as before but using 3 double qoutes to make everything inbetween not taken as a command
print(""" "The end", " or is it?", "keep watching!", 3 """)

## Normal print with double qoute to allow a single qoute inbetween
print("today is a 'good day' to learn python")
## Normal print with single qoute
print('python is fun')
## Normal print with double qoutes
print("python's string are easy to use")
## Normal print with single qoutes and inbeteen double qoutes
print('we can even include "quotes" in strings')
## Normal print with double qoutes in between 2 values and making the operator be ignored creating a space
print("hello" + " world")

greeting = "hello"
name = input("please enter your name")
print(greeting + name)

#if we a space, we can add that too
print(greeting + ' ' + name)

##########################

splitString = "this string has been\nsplt over\nseveral\nlines"
print(splitString)

#tabbed string to make space between numbers with a print to printout the value
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "no, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"no, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,..he's resting". """)

anotherSplitString = """This string has been \
split \
several \
lines"""

print(anotherSplitString)
#########

print("Number   1\tThe Larch")
print("Number   2\tThe Horse Chestnut")

########################################

# name is = to varable
# input is = to function
# print(name) is = to printing out the varable
# what is your name?" is = to string
# user input is = to value

# input is the function "what is your name?" is the string and when the user inputs a value
# the function is now the value the user inputed and we assigned the function to the varable
# then we call it out with the print function.
###################
# name = input("what is your name?")
# print(name)
###################
#name = "jack"
#print(name)
###################
name = input("what is your name")
length = len(name)
print(name, "has", length, "number of letters")
###################