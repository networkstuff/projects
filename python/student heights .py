#fruits = ["Apples", "Peach", "Pear"]

#for fruit in fruits:
# print(fruit)
#    print(fruit + "pie")
#  print(fruits)

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
#    total_height += height
    print(height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
#print(number_of_students)

average_number_in_height = round(total_height / number_of_students)
print(average_number_in_height)
