numbers = []

for i in range(3):
    numbers.append(input("Enter number: "))
max = 0
for i in numbers:
    max = i
    if (i > max):
        max = i

print(f'Maximum value is {max}')



