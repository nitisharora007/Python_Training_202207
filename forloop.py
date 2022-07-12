

# Coffee machine:

coffee_options = {"C": 0, "L": 0, "A": 0, "W": 0}
counter = 0

while counter <= 10:

    print(f"Number - {counter}")
    counter += 1

print(coffee_options)
print(coffee_options.values())

total = 0
for i in list(coffee_options.values()):
    total += i

print(total)

