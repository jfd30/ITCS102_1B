import random 

print("--Welcome to the Number Guessing Game--")

rn = random.randint(1, 3)
tries = 0
cont = True

while cont == True:
    value = eval(input("Input any number: "))
    if value != rn:
        tries += 1
        print("Sorry, Please Try Again")
        continue
    elif value == rn:
        print("CONGRATULATIONS, You got it right")
        break
print(f"You only took {tries} tries")
