'''
    If else condition block

    if <condition/expression>:
        <Statements>
    elif <condtion/expression>:
        <Statements>
    else:
        <Statements>
'''

student_age = 15


if student_age < 10:
    print(f"Student is elgible for standard 7")
else:
    print(f"Student not eligible for standard 7")

print("Student eligibility test result completed") 


'''
    
    Person salary -> Parameter

    Salary          Group   Card Eligible
     <= 500           A     (Silver)
     <= 1000          B     (Gold)
     <= 4000          C     (Diamond)
      -               D     (Elite)

'''

salary = 300000
if salary <= 500:
    print(f"Person belongs to group A")
elif salary <= 1000:
    print(f"Person belongs to group B")
elif salary <= 4000:
    print(f"Person belongs to group C")
else:
    print(f"Person belongs to group D")

salary = 300000
group = ""
elgible_card = ""
if salary <= 500:
    group = "A"
    elgible_card = "Silver"
elif salary <= 1000:
    group = "B"
    elgible_card = "Gold"
elif salary <= 4000:
    group = "C"
    elgible_card = "Diamond"
else:
    group = "D"
    elgible_card = "Elite"

print(f"Person belongs to group {group} and Card: {elgible_card} ")


'''
    Combining conditions:
        salary + age => card

        and -> condition1 + condition2 => True, otherwise False
        or -> condition1/condition2 => True, False - when both conditons fails

'''

age = 45
salary = 300000
if salary > 4000 and age > 35:
    print("Eligible for the card:")
else:
    print("Not Eligible")
