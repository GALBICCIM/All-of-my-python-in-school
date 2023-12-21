for y in range(2, -3, -1):
    for x in range(-2, 3):
        if y == x:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
# y = x