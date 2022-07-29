'''
    Functions - predefined templates for a piece of code that are re-usable

    Syntax: 
        def <function_name>(<parameters>):
            <Statements>

        <parameters> can vary from 0 - n
'''

def welcome_meesage(name):
    print(f"Welcome {name} to the meeting")


welcome_meesage("Nikunj")
welcome_meesage("Abram")


# Function w/o parameters

def welcome_message_wp():
    print("Welcome to the meeting")


welcome_message_wp()


# len - in-built functions of the python
ls = [1,2,3,4,5,6]

print(f"Length of list: {len(ls)}")

ls.append(8)
print(f"Length of list: {len(ls)}")

ls.extend([7,9,10,11])
print(f"Length of list: {len(ls)}")
print(f"Length of list: {ls}")


# Optional paramters - Default value associated with parameters

def welcome_meeting(name="all"):
    print(f"Welcome {name} to the meeting")

welcome_meeting("Josia")
welcome_meeting()


# Arbitarary Parameters - * in arguments of function definition

def sum(*nums):
    print(f"Nums: {nums}")

    sum = 0
    for elem in nums:
        sum += elem
        print(f"Val of elem is {elem}")

    return sum

val = sum(1,2,3,4, 18, 12, 10)
print(f"Sum is: {val}")


# Keyword based agruments
# lambda 


# 14 July - Return keyword, lambda

'''
    # Functions -> code reuse, Processing
    Processing function -> black box -> input => output

    Custom function
    sum(1,2,3) => 1 + 2 + 3 => 7 => within function definition, 

    return Object

    Shopping Mart => Purchased Objects => getBill([Obj1, Obj2]) => Calculates => Return the amount


    amount = getBill([Obj1, Obj2, Obj3])
'''

print("*"*90)

def getBill(items):

    total = 0
    for elem in items:
        total += 1
    
    print(f"Total amount is {total}")
    return total


fruits = ["apple", "banana", "kiwi"]

bill_amount = getBill(fruits)
print(f"Hey !!! Your total amount is {bill_amount}")


items = 10
items = [1,2,3]
items = (1,2)

print("*"*95)

def first_even(num):

    for i in range(1, num):
        print(f"Processing {i}")
        if i%2 == 0:
            print("Function is returning")
            return i
            print("Function returned")

even = first_even(10)
print(f"First even is {even}")

'''
    isPrime -> whenever condition fails, return 
'''


def isPrime(num):

    for i in range(2, num):
        
        if num%i == 0:
            return False

    return True

while True:
    num = int(input("Please provide a number to validate prime or not: "))
    if num == 0:
        break
    prime = isPrime(num)
    print("*"*100)

    print(f"Is {num} a prime - {prime}")

'''
if <expression>: 
    <statement1>
else: 
    <statement>

<value> if <expression> else <Value>
'''

flag = True if num %2 == 0 else False 

if num %2 == 0:
    flag = True
else:
    flag = False



lambda x : x/3 if x%3 == 0 else x

    ######### SIMILAR ##################

def func(x):

    if x%3 == 0:
        return x/3
    else:
        return x

    ######### SIMILAR ##################


def func(x):

    return x/3 if x%3 ==0 else x 




# Lambda functions - one liner function test a certain, return it 
# Anonymous functions ->  don't have a name

# Syntax:
#   lambda <params> : <expression>
#   lambda x,y: y%x == 0
# 
#   def func(x, y):
#       return y%x == 0      
#     
#       
#  

def isEven(num):

    if num%2 == 0:
        return True

def isEven(num):

    return num%2 == 0

# 
isEven = lambda num: num%2 == 0

sum = lambda x,y,z: x + y +z





total = sum(1,2,3)
total = sum(5,7,9)


is_even = even(10)
is_even = even(20)

is_divisble = lambda x,y: int(y/x)

print(f"2,10 - {is_divisble(2,10)}, 3,80 - {is_divisble(3,80)}") 
# x -2, y 10, 10%2 => 0, 
# x - 3, y 10, 10%3 => 1






