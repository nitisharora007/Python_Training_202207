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

fruits = []
veggies = []

while True:

    #cat = input("enter the cat(veg/fruit): ")

    inp_name = input("Enter the name: ")
    
    if inp_name == "break" or inp_name == "end" or inp_name == "eol":
        break

    fruits.append(inp_name.lower())
# lower - lower case all characters in string
# upper - Upper case all characters in string

    # Categorization logic - which will input from the user to specific 

#    if :
#        veggies.append(inp_name)
#    else:


print(fruits)
print(veggies)

'''
    Unique - set
'''

print(type(fruits))

uq_fruits = set(fruits)

print(f"Unique fruit name: {uq_fruits}")

