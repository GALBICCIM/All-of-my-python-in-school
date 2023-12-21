for y in range(0, -6, -1):
    for x in range(-5, 6):
        if y <= -1 * abs(x):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
# y ≤ -|x|