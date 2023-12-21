def convert(numbers):
    two = bin(numbers)
    eight = oct(numbers)
    sixteen = hex(numbers)
    
    A = """2 진수 : {0}
8 진수 : {1}
16 진수 : {2}""".format(two, eight, sixteen)

    return A


print(convert(18))