print("Odd number Summation")

sum = 0

for x in range(0, 7, 1):
    numbers = eval(input("Enter any number ---> "))
    if numbers % 2:
        sum += numbers
print("The sum of all given odd is", sum)
