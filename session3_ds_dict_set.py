
'''
    List:
        Val1, val2, Val3
        Mutuable
    Dict: 
        Sequence of elements
        Key1:val1, Key2: Val2
        Start with { and ends with } separated via comma

        Keys should be immutable (string, tuple) and case-sensitive

        Access: Via keys

        Mutuable in nature
'''

d1 = { "training_name": "Python", "session": "second day" }
print(d1)

print(d1["training_name"])
print(d1["session"])

d1["session"] = "Day for DS"

print(d1)

emp = {
    "1": "Nitish",
    "2": "Raj",
    "3": "Anand",
    "4": "Bryte",
    "5": "Dipika"
}

print(emp)

emp["1"] = {"fname": "Nitish", "lname": "Arora"}
emp["2"] = {"fname": "Raj", "lname": "Kaur"}
emp["3"] = {"fname": "Anand", "lname": "Prjapati"}
emp["4"] = {"fname": "Bryte", "lname": "Abraham"}
emp["5"] = {"fname": "Dipika", "lname": ""}

print(emp["4"]["lname"])


emp1 = {"fname": "Nitish", "lname": "Arora", "lang": "Python"}
emp2 = {"fname": "Raj", "lname": "Kaur"}
emp3 = {"fname": "Anand", "lname": "Prjapati"}
emp4 = {"fname": "Bryte", "lname": "Abraham"}
emp5 = {"fname": "Dipika", "lname": ""}

# Dictionary of dictionary
emp = {
    "1": emp1,
    "2": emp2,
    "3": emp3,
    "4": emp4,
    "5": emp5
}

# List of dictionary
emp_ls = [emp1, emp2, emp3, emp4, emp5]


print("-"* 79)
print(f"Type of emp: {type(emp)}, emp_ls: {type(emp_ls)}  ")

print("-"*80)
print(f"Employee: {emp['2']}")
#emp["1"]
print(f"Employee: {emp_ls[1]}")
#emp_ls[0]

print("-"*80)
print(emp)
print("-"*80)
# {"": {}, }


print("-"*80)
print(emp_ls)
print("-"*80)
# [ {}, {}, {} ]




# Dict function:
# {key: value, key: value, key: value}

# in-built function: keys, values

print(f"Emp object having properties: {emp2.values()}")



'''
    Set: 
        Sequence of elements, similar to list
        every element is unique in the set

        Define: starts with bracket {} and separated via comma

        Access: Used via index (numeric)
'''

print("-------- Set------------")
fruits = {"apple", "banana", "grapes"}

print(fruits)

fruits = {"apple", "banana", "grapes", "apple"}
print(fruits)


ls = ["apple", "banana", "grapes", "apple", "grapes", "guava"]

print(f"List: {ls}")
print(f"Set: {set(ls)}")
