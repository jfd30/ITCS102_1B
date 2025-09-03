name = input("What's your name?: ")
fare = int(input("What's your fare fee?: "))

print("20% discount if you are a student")

student = input("Are you a student? yes or no?: ")

if student.lower() == 'yes':
    percent = (20 * fare) / 100
    print("You're discounted!")
    print("Your total fee after discount is: ", fare - percent)
else:
    print("You're not elligible for discount :(")
