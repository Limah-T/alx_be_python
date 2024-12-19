size = int(input("Enter the size of the pattern: "))
count = 1
while count <= size:
    for n in range(size):
        print("*", end=" ")
    print()
    count += 1