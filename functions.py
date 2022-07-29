
'''
    Functions - Re-usable Block of code and will be executed as & when they are called.

    Define - Definition
    Call - Invocation of function        

    def function_name(param1, param2 .... ):
        statement1
        statement2

    function_name(param1, param2)
'''

# Basic function with no parameter
def func():
    print("Function called")

def func2():
    print("Function 2 called")


# Calling the function
#func()
#func2()
#func()

def welcome_message(name):
    print(f"Welcome {name} to the club")


#welcome_message("Ramesh")
#welcome_message("Suresh")

# Ways of passing parameters
# Positional arguments
# 
def sum(a, b=10):
    print(f"A - {a}, B - {b}")
    total = a + b
    print(f"Total - {total}")

#sum(1,2)

#sum(4,5)


# Invalid
#sum(4,5,6)
#sum(4, 4)


# Keyword based arguments, function calling, function_name(param1 =val1, param2 =val2)
#sum(b=10, a=5)

#sum(a=5, b=5)

'''
    Another way of defining the function
    Optional Parameters

'''

#sum(4)



'''
    Arbitary arguments *args
    Keyword based arguments    **kargs
'''


def mul(*args):

    print(type(args))
    print(args)
    total = 1
    for arg in args:
        print(arg)
        total *= arg
    print(f"Total - {total}")

#mul()
#mul(1)
#mul(1,2)
#mul(1,2,4)
#mul(1,4,6,8)


def name(**kwargs):

    print(f"Kwargs - {kwargs}, Type - {type(kwargs)}")     # dict

    full_name = ""

    if "fname" in kwargs:
        full_name += kwargs["fname"]
    if "lname" in kwargs:
        full_name += kwargs["lname"]

    print(full_name)


#name(fname="Ramesh")
#name(fname="Tic", lname="Tac")


'''
    Laptop acc - Headphone, Webcam, Joystick, Trackpad

'''

def laptop_acc(name, **kwargs):

    print(kwargs)
    print(f"{name} is having - {list(kwargs.keys())}")

    if "headphone" in kwargs:
        print("Wow!! He/She is having a headphone")

laptop_acc("Ramesh", headphone="yes", webcam="yes")       # {"headphone": "yes", "webcam": "yes"}
laptop_acc("Suresh", trackpad="yes")                      #  {"trackpad": "yes"}



# When we are not clear with function definition
def func():
    pass


func()

'''
    Create a function named isPrime which will print whether number is prime or not
        Take the default parameter in the definition of the function as 1.


    Create a function named multiply which will take the arbitary arguments and print the total.

'''





# 13 Jul - Return & args/kwargs, passing the list