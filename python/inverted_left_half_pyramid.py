rows = 5

for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")

    print()
