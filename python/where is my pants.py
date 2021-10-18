import random
shopping = ["shoes", "pants", "tshirt", "jacket"]

a = random.choice(shopping)

if "pants" in str(a):
    print("pants are found")
else:
    print("pants are not found")
