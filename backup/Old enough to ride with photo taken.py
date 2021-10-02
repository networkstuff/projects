### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: tall enough to ride + age and if you want a photo that was taken.

height = int(input("what is your hight: "))
bill = 0

if height >= 120:
    age = int(input("how old are you: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Ride is free")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("do you want photos? Just type Y or N")
    if wants_photo == "Y":
        bill = bill + 3  # or bill += 3 but leaving as is for easy reading.

    print(f"your final bill is ${bill}")

else:
        print("sorry you can not ride, too short")