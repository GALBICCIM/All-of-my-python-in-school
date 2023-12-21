for y in range(5, -6, -1):
    for x in range(-5, 6):
        if abs(y) + abs(x) <= 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()