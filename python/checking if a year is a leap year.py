# Author: Ivan V
# objective: For presentation purpose only

year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap tear")