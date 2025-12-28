for jay in range(1,11, 1):
    for a in range(11, jay, -1): 
        print(" ", end=" ")
    for b in range(1, jay, 1):
        print("*", end=" ")
    for q in range(1, jay, 1):
        print("*",end=" ")
    print()

for e in range(1, 11, 1):
    for g in range(1, e, 1):
        print(" ", end=" ")
    for o in range(11, e, -1):
        print("@", end=" ")
    for b in range(10, e, -1):
        print("@", end=" ")
    print()
