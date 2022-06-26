'''
    List
        Definition: It starts with square(opening) bracket and close with square bracket

        Elements are separated by comma
        
        Mutuable data types

        Access: Referred 
'''
ls = [1,2,3, 'Python Training']

ls2 = []    # Empty list

# List elements are referred using the Index (indices)
# Always start with zero

ls = ['C#', 'Java', 'PHP', 'Python', 'Node', 'React']
#        0,      1,      2       3       4       5

ls.insert(2, 'Javascript')

# After insert
# ls = ['C#', 'Java', 'Javascript', 'PHP', 'Python', 'Node', 'React']
#        0       1       2           3       4       5       6

ls.insert(0, 'Javascript')
ls.insert(0, 'Javascript')
ls.insert(0, 'Javascript')


print("-"*50)
print(ls)
print("-"*50)

print("-"*50)
elem = ls.pop()
print("Element Removed: ", elem)
print(ls)
print("-"*50)


# Professional Journey - List of companies C1, C2 

# List elements ranges from 0 - n
compa = []
compa = ['Info', 'Wip', 'TC']


print("-"*50)
print(compa)
compa[0] = 'Infi'
print(compa)
print("-"*50)

'''

Tuple
    Define: Starts with brackets '(' and close with ')'
    
    Elements are separated with comma
    
    Non-mutable - Cannot modify the element at specified index

    Tuples are faster in processing - At the time of assignment, no. of elements are fixed 
    and hence space is allocated at the time of definition.
 '''


tup = ('Info', 'Wip', 'TC')
#        0       1       2
print("-" * 80)
print(tup)
print('-'*50)


tup = (1,2, 'Python')
print("-" * 80)
print(tup)
print('-'*50)
