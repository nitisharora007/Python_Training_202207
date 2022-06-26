name = "Josia"
# String - Collection of characters 
# Access  - via Index

#   J o s i a
#   0 1 2 3 4

print(f"Value at index 2: {name[2]}")

ls = ["PHP", "Python", 1, True, 12.3333]
tup = ("PHP", "Python", ls)
st = {"PHP", "Python"}
dct = {"lang1": "PHP", "lang2": "Python"} 
stg = "PHP"


print(f"Values: List: {ls[1]}, tuple: {tup[0]}, dct: {dct['lang1']}, stg: {stg[2]}")


print("-"*30)
print(tup)
print("-"*30)

tup[2][0]="Basic Python"


tup[0] = "Lang"
print("-"*30)
print(tup)
print("-"*30)
