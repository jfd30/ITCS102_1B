#odd and even summation
name = input("Enter your name --> ")
odd = 0
num_name = ""
even = 0
even_name = ""

while True:
    num = eval(input("Enter a random number: "))
    if num == 0:
        print(f"Program STOPS!\nHello {name}, \nThe total of ODD is: {odd}\nThe ODD components are: {num_name}")
        print(f"The total of EVEN is: {even}\nThe EVEN components are: {even_name}")
        break
    elif num % 2 == 1:
        print("This is an ODD number!")
        odd += num
        num_name += str(num) + " "
        continue
    else:
        if num % 2 == 0:
            print("This is an EVEN number!")
            even += num
            even_name += str(num) + " "
        continue
