def wc(string):
    count = 0
    
    for i in string:
        if i != " ":
            count += 1
        
        elif i == " ":
            pass
        
    return count

print(wc("박승원 박승원 박승원"))