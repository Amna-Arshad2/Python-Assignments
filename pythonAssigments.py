""""
# Assignment 1B
1. Write a Python program to print the following string in a specific format (see the output).
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

"""

# Solution :
print('''
Twinkle, twinkle, little star,
         How I wonder what you are!
                 Up above the world so high,
                 Like a diamond in the sky.
Twinkle, twinkle, little star,
         How I wonder what you are
''')
            
                # OR
print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are\n")                


# 2. Write a Python program to find out what version of Python you are using.
# Solution : 
import sys
print(f'You are currently using {sys.version} Python version \n')


# 3. Write a Python program to display the current date and time
# Solution :
import datetime as dt
curr_time = dt.datetime.now().time().strftime('%H:%M:%S')
curr_date = dt.datetime.now().date().strftime('%d/%m/%Y')
print(f'Current Date is: {curr_date} & Current Time is: {curr_time}')


# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Solution :
radius = float(input('Enter circle Radius: '))
area = 3.14 *(radius**2)
print(f'The area of circle with radius {radius} is: {round(area, 3)} sq.meter')


# 5. Write python programme which accepts user first name and last name and print them in reverse order with a space between them. 
# Solution : 
first_name = input('Enter your First name: ')
last_name = input('Enter your Last name: ')
full_name = last_name + " " + first_name
# full_name = f'{first_name[::-1]} {last_name[::-1]}' 
print('Reversed name: ', full_name)


# 6. Write python program which takes two input from users and print them addition
# Solution :
num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))
print(f'Sum of {num1} and {num2} is: {num1 + num2} \n')


# 7. write a programme that takes 5 inputs from user for different subject's marks, Total it and generate marksheet using grades
# Solution : 
courses = ['English','Urdu','Maths','Biology','Physics']
total_marks = 500
obtained_marks = []
marks_sum = 0
grades =[]
counter = 0

for course in courses:
    marks = float(input(f'Enter obtained marks in {course}: '))
    if  marks <0 or marks >100 :
        print('Please Enter marks between 0 - 100')
        break
    elif  marks >=90 and marks <=100 :
        grades.append("A+")
    elif marks >=80 :
        grades.append("A")
    elif marks >=70 :
        grades.append("B")
    elif marks >=60 :
        grades.append("C")
    elif marks >=50 :
        grades.append("D")
    elif marks >=33 :
        grades.append("E")
    elif marks < 33 :
        grades.append("F*")
        counter += 1
    else :
        print(f'Invalid Input!')
    
    obtained_marks.append(marks)
    marks_sum += marks
    
def marksheet(courses, obtained_marks, grades) :
    percentage = (marks_sum/total_marks)*100 

    print("-------------Student's Marksheets----------------------------\n")
    print('Subject Name\tTotal Marks\tObtained Marks\tGrade \n')
    for i in range(len(courses)):
        print(f'{courses[i]}\t\t100\t\t{obtained_marks[i]}\t\t{grades[i]} \n')

    print('-------------------------------------------------------------')
    print(f'Total \t\t{total_marks} \t\t{marks_sum}\t\t{round(percentage, 2)} % \n')
    
    if counter >=3 :
        print(f'You have failed* in {counter} subjects. :(')
        
marksheet(courses, obtained_marks, grades)      


# 8. write a programme which take input from user and identify that given number is even or odd
# Solution :
# number = int(input('Enter any integer: '))  # No Decimal numbers
# if number%2 == 0 :
#     print(f'{number} is even number')
# else:
#     print(f'{number} is odd number')

# 9. Write a program which print the length of the list?    
# Solution: 

newList = [10, 20, 30, 40, 50,' ', 60]
print(f'Length of list is : {len(newList)}')


# 10.Write a Python program to sum all the numeric items in a list?
# Solutions: 

li = [100, 200, 300, 400, 500, 600]
sum = 0
for item in li:
    sum += item
print(f'Sum of all numbers are : {sum}')  


# 11.Write a Python program to get the largest number from a numeric list.
# Solution:

li = [100, 200, 300, 400, 500, 600]
print(f'Lagest number of all numbers is : {max(li)}')  


# 12. Take a list, say for example this one:
# Write a program that prints out all the elements of the list that are less than 5.
# Solution:

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in list:
    if element < 5:
        print(element)

            
            ########### Assignment 4 #############

# 1. Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
# Solution: 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

op = input("Enter Mathmatical operator o perform: ")

if op == '+':
    sum = add(num1, num2)
    print(f'Sum of {num1} & {num2} is : {sum}')  
elif op == '-':
    sub = subtract(num1, num2)
    print(f'Difference of {num1} & {num2} is : {sub}')    
elif op == '/':
    div = divide(num1, num2)
    print(f'Division of {num1} & {num2} is : {div}')    
elif op == '**':
    pow = power(num1, num2)
    print(f'Power of {num1} & {num2} is : {pow}')  
else:
     if op not in ('+', '-', '/', '*', '**'):
        print("Invalid choice! please enter valid input")
    


# 2. Write a program to check if there is any numeric value in list using for loop
# Solution:

def has_numericVal(input_list):
    for item in input_list:
        if isinstance(item, (int, float)):
            return True
    return False

myList = [120, 'Amna', 3.14, 'Arshad', 300, False]
result = has_numericVal(myList)

if result:
    print("The list contains at least one numeric value.")
else:
    print("The list does not contain any numeric value.")


# 3. Write a Python script to add a key to a dictionary.
# Solution: 

myDict = {'first Name': 'Amna', 'last Name': 'Arshad', 'city': 'Karachi'}

new_key = 'occupation'
new_value = 'engineer'

myDict[new_key] = new_value
print("Updated dictionary:", myDict)


# 4. Write a Python program to sum all the numeric items in a dictionary.
# Solution: 

def sum_numeric_items(dictionary):
    total_sum = 0
    
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total_sum += value
    
    return total_sum

data = {
    'a': 10,
    'b': 5.5,
    'c': 'hello',
    'd': 20,
    'e': 'world'
}

numeric_sum = sum_numeric_items(data)
print("Sum of numeric items:", numeric_sum)


# 5. Write a program to identify duplicate values from list.
# Solution: 

def find_duplicates(input_list):
    duplicates = []
    unique_values = set()

    for value in input_list:
        if value in unique_values:
            duplicates.append(value)
        else:
            unique_values.add(value)

    return duplicates

input_list = [10, 20, 30, 40, 50, 20, 60, 70, 80, 10]
duplicate_values = find_duplicates(input_list)
print("Duplicate values:", duplicate_values)



# 6. Write a Python script to check if a given key already exists in a dictionary
# Solution: 

def check_key_in_dictionary(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

if check_key_in_dictionary(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")