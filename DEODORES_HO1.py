some = (input("Enter a word: "))
k = len(some)
to = []
for i in range(1, k + 1, 1):
    ask = int(input(f"Enter number {i}:"))
    to.append(ask)
print(to)
print(f"The length of the word is {n}")
total = 0
for num in to:
    total = total + num
ave = total/n
print(f"The average of the number is {ave}")
if ave < k:
    print(f"The length of the word '{hello}' is less than the average.")
elif ave > k:
    print(f"The length of the word '{hello}' is greater than the average.")
elif ave == k:
    print(f"The length of the word '{hello}' is equal than the average.")
