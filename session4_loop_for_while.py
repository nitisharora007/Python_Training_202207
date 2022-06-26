'''
    for, while - Looping statements 
'''

# for loop
'''
    Syntax:
        for <obj> in <iteratable>:
            <Statements>
'''

# Input provided
students =          ["Alen", "Bo", "Sophia", "Joseph"]
# 1st Iteration:      stu
# 2nd Iteration:              stu
# 3rd Iteration:                     stu
# 4th Iteration:                             stu

students.append("Prasan")
students.append("h")

'''
    Via Looping 
'''

for stu in students:
    if len(stu) <= 2:
        print(f"Student Name: {stu}")


'''
    break - break the loop
    continue - continue to next iteration
'''

students.insert(2, "Bob")
print(students)


count = 0
for stu in students:
    count += 1
    if stu == "Bob":
        print("Bob found")
        break
        
print(f"Loop iterated {count} times")

nums = [1, 2, 3,4,5,6,7,8,9]


for elem in nums:
    print(f"Value of elem: {elem}")
    if elem %2 != 0:
        continue
    print(f"Even numbers: {elem}")

'''
    while - looping statement/instruction for iterating over the iterator object

    while <experssion/condition>:
        <Statements>
'''

num_count = 1

while num_count <= 5:
    print(f"Number: {num_count}")
    num_count += 1


# Infinite Loop
num_count = 1


while True:    
    num_count += 1

    if num_count > 100 and num_count < 1002:
        continue

    print(f"Number: {num_count}")
    
    if num_count == 1050:
        break