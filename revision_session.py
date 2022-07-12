'''
    Data Structures - int, bool, list, tuple, dict, set

    if/else - conditional block

    for, while - looping 
'''


''' 
    Input your name, age ->
        based upon the age it will display 

    For entering into bar, min age required is 18
    Mohan, 14 ->  Sorry Mohan!!! You have to grown up
    Krish, 24 -> Welcome Krish to the club
'''
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome {name} to the club")
else:
    print(f"Sorry {name} !!! You have to grown up")
'''
# Practice - Print the years that person has to come after that


'''
    Multiple if, else statement blocks

    IT Slabs - 
        If salary is lesser than or equal to 10K, person belongs to "Group A"
        If salary is greater than 10K and lesser than 50K, person belongs to "Group B"
        If salary is greater than 50K, person belongs to "Group C" 
'''

'''
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

person_cat = ""

if salary <= 10000:
    person_cat = "Group A"
elif salary > 10000 and salary < 50000:
    person_cat = "Group B"
else:
    person_cat = "Group C"

print(f"Hi {name}, Your category is {person_cat}")
'''

'''
    Collect the name of fruits from the users - List
    End button - to close down the capture 
        By typing end/break in the fruit name
'''

# List - Data structure, collection of items/elements

from importlib.abc import ExecutionLoader
from re import M
from tokenize import Name
from typing import Dict


fruits = []
veggies = []


# lower - lower case all characters in string
# upper - Upper case all characters in string

    # Categorization logic - which will input from the user to specific 

#    if :
#        veggies.append(inp_name)
#    else:


#print(fruits)
#print(veggies)

'''
    Unique - set
'''

#print(type(fruits))

uq_fruits = set(fruits)

#print(f"Unique fruit name: {uq_fruits}")

'''
    Agenda:

        Dict from input - Columns
            
        Pythonic ways to write up
            List comprehension
            Dict comprehension

        Functions
            What & why
            Arguments - Positional, Keyword, Optional, Default
                        Args, Keyword-based arguments

'''

# List/Tuple - Collection of items/elements
    # Acces - index (indices)

# Dict - Key-value based collection of items
    # Access - Key

'''
Spreadsheet - 
    Rows & Columns

Columns - Keys of Dict
Row - Element in a dict

Rows -
    row1
    row2
    .
    .
    .
    rown

List - collection of item/element - dict

Name    Age     Gender
Nitish  23      Male                -> Element 1
Ramesh  34      Male                -> Element 2
Sophia  56      Female              -> Element 3

'''

row1 = {"Name": "Nitish", "Age": 23, "Gender": "Male", "NewKey": "val"}
row2 = {"Name": "Ramesh", "Age": 34, "Gender": "Male"}
row3 = {"Name": "Sophia", "Age": 56, "Gender": "Female"}


#print(f"Age - {row1['Age']}")
#print(f"Name - {row2['Name']}")
#print(f"Gender - {row3['Gender']}")

# Keys and values access from dict
#print(f"Keys: {row1.keys()}, Values - {row1.values()}")


'''
    Spread-sheet, List of dict
'''

spread_sheet = []

while True:

    name = input("Enter the person name: ")

    if name == "eol":
        break 

    age = int(input("Enter the age: "))
    gender = input("Enter the gender: ")


    row = {"Name": name, "Age": age, "Gender": gender}

    spread_sheet.append(row)

print(spread_sheet)

# enumerate - Iterate over the list & dict: 
# list - index
# dict - key

'''
keys() - Name, age & gender
    Name    age     gender          -    Keys in dict element - printed only for 1st record
    Nitish  23      M
    Ramesh  45      M 

'''

for idx, row in enumerate(spread_sheet):

    # Print the header - keys() - header - ['Name', 'Age', 'Gender']
    if idx == 0:
        header = list(row.keys())
        print(f"{header[0]} :: {header[1]} :: {header[2]}")

    print(f"{row['Name']} :: {row['Age']} :: {row['Gender']}")


''' 
    List comprehension - pythonic way to generate/filter the list

    Filter out a list of numbers  - odd, even
'''

#[1,2,3,4,5, ... 99]
# odd number and even number
# odd = [1,3,5,7]
# even = [2,4,6]

odd = []
even = []

for i in range(1, 100):
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"Odd - {odd}")
print(f"Even - {even}")

#odd = [ <Iteraable> {<if_condition>} ]

odd2 = [i  for i in range(1, 100) if i % 2 != 0]
even2 = [elem for elem in range(1,100) if elem %2 == 0]

print(f"Odd - {odd2}")
print(f"Even - {even2}")

# Dict Comprehension
# Dict {1:1, 2: 4, 3: 9}
print("*"*90)
sq_nums = {elem: elem*elem for elem in range(1,10)}
print(list(sq_nums.values()))
print(sq_nums)

sq_nums_ls = [elem*elem for elem in range(1, 10) ]
print("*"*90)
print(sq_nums_ls)





