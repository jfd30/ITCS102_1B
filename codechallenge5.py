factorial = 1
number = eval(input("enter number"))
for x in range(number, 0, -1):
    factorial *= x
print("the factorial of your number is", factorial )    