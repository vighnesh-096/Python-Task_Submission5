# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1. Creates a dictionary where student names are keys and their marks are values.
# 2. Asks the user to input a student's name.
# 3. Retrieves and displays the corresponding marks.
# 4. If the student's name is not found, display an appropriate message.

keys = ["John","Sam","Joy"]
values =[10,90,80,70]
student_name = dict(zip(keys,values))
name = input("Enter a name")
if name in student_name:
    print(f"Marks of {name} is {student_name[name]}")
else:
    print(f"Not found the Name")

