inputFile = open("./test/input.txt", "r", encoding = "UTF-8")
outputFile = open("./test/output.txt", "w", encoding="UTF-8")

lines = inputFile.readlines()


for i in lines:
    print(i.strip("\n"))


outputFile.write("This is output.txt\n")
outputFile.writelines(lines[1:])