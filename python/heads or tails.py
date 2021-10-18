### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: simple heads or tails xD

import random

input("heads or tails?\n")
a = random.randint(0, 1)

if a == 0:
    print(f"it is heads")
if a == 1:
    print(f"it is tails")
