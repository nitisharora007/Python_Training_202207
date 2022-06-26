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