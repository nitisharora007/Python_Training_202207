'''
Data Structure - Structure (organization) of data to hold the pieces of data

Categories of DS (in Python):
- Iteratable: multiple elements/items which can be iterated
    list, dict, tuple, string
    
    -- Mutable: Elements can be changed within the data structure
                list, dict
    -- Non-mutable: Elements cannot be changed within the data structure
                string, tuple

- Non-iteratable: single element/item which cannot be iterated
    int, bool, float, complex
'''


age = 23 # integer
name = 'Nitish' # string

# Boolean data type
is_valid = True     # boolean
is_valid = False    # boolean


'''
    String
    Starts with quote(single/double) and ends with same quote(single/double) respectively
    Sequence/Collection of characters
'''

name = "Nitish"
training_name = 'Python'

print(name," is having",training_name," session")
print(f"{name} is having {training_name} session")

fname = "Raj"
lname = "Kaur"

full_name = f"{fname} {lname}"
print(f"1st way full name: {full_name}")
full_name = fname + " " + lname
print(f"Another way full name: {full_name}")

print(f"String chars: {fname[0]}, {fname[1]}, {fname[2]}")
print(f"Length of Full Name: {len(full_name)}")

# Below line raise the exception for assignment as string are immutable
#fname[0] = 'K'


'''
    List: list(object)
    Set: set()
    Tuple: tuple()
    dict: dict(list[()])
'''

print(" "*80)
ls = ["Php", "Python", "C#", "Python", "Java", "Php"]
print(f"List: {ls}, Set: {set(ls)}, Tuple: {tuple(ls)}")


