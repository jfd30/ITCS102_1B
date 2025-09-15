def sum_of_odd_numbers():
    numbers = []
    print("Please enter 7 numbers:")
    for _ in range(7):
        num = int(input("Enter a number: "))
        numbers.append(num)
    
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    
    print("Entered numbers:", numbers)
    print("Sum of odd numbers:", odd_sum)

sum_of_odd_numbers()
