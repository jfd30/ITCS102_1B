some = (input("Enter a word: "))
n = len(some)
nsan = []
for i in range(1, n + 1, 1):
    ask = int(input(f"Enter number {i}:"))
    nsan.append(ask)
print(nsan)
print(f"The length of the word is {n}")
total = 0
for num in nsan:
    total = total + num
ave = total/n
print(f"The average of the number is {ave}")
if ave < n:
    print(f"The length of the word '{ilan}' is less than the average.")
elif ave > n:
    print(f"The length of the word '{ilan}' is greater than the average.")
elif ave == n:
    print(f"The length of the word '{ilan}' is equal than the average.")
