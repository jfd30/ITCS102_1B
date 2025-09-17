say = input("What do you want your parrot to say?--> ")
repeat_input = input("How many times should the parrot squawk it? --> ")

if repeat_input.isdigit():
    repeat = int(repeat_input)
    for x in range(repeat, 0, -1):
        print("Squawk!", say)
else:
    print("You did not enter a number for the repeat count!")
