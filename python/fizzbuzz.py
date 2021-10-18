for number in range(1, 101):

    if (number % 3) == 0 and number % 5 == 0:
        print(f"fizzbuzz")
    elif (number % 3) == 0:
        print(f"fizz")
    elif (number % 5) == 0:
        print(f"buzz")
    else:
        print(number)
