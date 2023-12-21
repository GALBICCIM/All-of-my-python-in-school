inputTXT = open("input.txt", "r", encoding = "UTF-8")
outputTXT = open("output.txt", "w", encoding = "UTF-8")

readInput = inputTXT.readlines()
tencount = 0
fivecount = 0


for tenwordlen in readInput:
    if len(tenwordlen.strip("\n")) <= 10:
        tencount += 1
    
    else:
        pass


for fivewordlen in readInput:
    if len(fivewordlen.strip("\n")) <= 5:
        fivecount += 1
        
    else:
        pass
    

for writeword in readInput:
    if len(writeword.strip("\n")) <= 10:
        outputTXT.write(writeword)


print(tencount)
print(fivecount)