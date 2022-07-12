

from operator import index


ls1 = [elem for elem in input("Enter the names: ").split()]
ls2 = [int(elem) for elem in input("Enter the marks: ").split()]

print(ls1)
print(ls2)

ls1[0] = "Ramesh"
print(ls1)
print(ls2)

ls2.sort()

'''
ls1 -> Bucket   => Append 
ls2 -> Bucket   => 

Bucket of balls
Color: size

size => user input
color: size =>
Blue: 10
Green: 12
Yellow: 1

Association => Dict Data type
Name: marks
Ram: 23

'''

buckets = {"Blue": 12, "Green": 10, "Yellow": 3}

print(buckets.values())

sizes = [12, 10, 3]
print(sizes)

for key,val in enumerate(sizes):
    print(f"Key - {key}, Value - {sizes[key]}")

buckets = {"Blue": 12, "Green": 10, "Yellow": 3}
max_size = 0
elem = {}

for key in buckets:

    print(f"Key - {key}, Value - {buckets[key]}")
    if buckets[key] > max_size:
        elem = {'color': key, "size": buckets[key]}
        max_size = buckets[key]

print(elem)