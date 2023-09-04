num = input("Please enter a number: ")

countDigits = 0
max = num[1]
min = num[1]
for i in range(len(num)):
    countDigits += 1
    if num[i] > max:
        max = num[i]
    if num[i] < min:
        min = num[i]

print(f'Number of digits in the given number is: {countDigits}')
print(f'Smallest number is: {min}')
print(f'Highest number is {max}')

