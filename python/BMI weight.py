### Author: Ivan V
### purpose: for educational/presentation purposes ONLY!
### explanation: tip calculator


class bold_color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = (weight / height ** 2)

BMI = round(a)

if BMI >= 35:
    print("your BMI is:", BMI ,bold_color.RED,"you are clinically obese.")

elif BMI >= 30:
        print("your BMI is:", BMI ,bold_color.RED,"you are obese." )

elif BMI >= 25:
        print("your BMI is:", BMI ,bold_color.YELLOW, "you are slightly overweight")

elif BMI >= 18.5:
        print("your BMI is:", BMI ,bold_color.GREEN, "you are normal weight")

elif BMI < 18.5:
    print("your BMI is:", BMI , "you are",bold_color.RED,"underweight")
