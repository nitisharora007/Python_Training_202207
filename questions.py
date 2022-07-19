'''
Here are the below questions:
Q1) Given a list of number in the sequence, print the numbers in reverse.

lst = [1,2,3,4]
lst2 = [4,3,2,1]
O/P:
4
3
2
1

Q2) Given a string (list of characters), you need to check whether the string is palindrome or not.
Palindrome string if one half of the string is the reverse of the other. 
For example, abccba is palindrome as 
first character and last character is a
second character and second last character is b
third character and third last character is c

Q3) Create a function which will print the factorial of a given number.

Q4) Write a function to count the odd and even number in a list which is provided as a 
parameter to function.

'''

# first 10-12 mins - your practice
# last 3 mins - i will work on solution


lst = [23,45,67,89]

i=0
while i < len(lst):
    print(lst[i])
    i = i+1

print("**"*20)
print("Reverse order::  ")

i = len(lst) - 1
while i >=0:
    print(lst[i])
    i = i -1

print("**"*20)
print("Palindrome ::  ")
'''
    Palindrome: first character == last character, second character == second last character and so on
'''
s = input("Check whether string is palindrome or not: ")
'''
        length = 6

#       a b c c b a
#       0 1 2 3 4 5     => i -> 0, 1
#                       => j -> 5, 4

#       a b c d d c b a

#       a b c d x c b a

#       a  b  a 

'''
i = 0
j = len(s) - 1
flag = True

while i < len(s):

    if s[i] != s[j]:
        flag = False
        break

    i = i + 1
    j = j - 1

if flag:
    print(f"{s}: Palindrome")
else:
    print(f"{s}: Not palindrome")


print("*"*90)
print("Factorial:: ")

'''
    Factorial = Multiply the number(s) encountered in range
    fact(5) = 1 * 2 * 3 * 4 * 5                 => 120
    fact(8) = i * 2 * 3 * 4 * 5 * 6 * 7 * 8     => 40320

'''

def fact(num):

    i = 1
    res = 1
    
    while i <= num:
        res = res * i
        i = i + 1

    return res

n = int(input("Enter the number: "))
print(f"Factorial({n}) is {fact(n)}")

