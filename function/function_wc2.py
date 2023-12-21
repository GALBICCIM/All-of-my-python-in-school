def wc2(string):
    count = 0
    
    for i in string:
        if i == " ":
            count += 1
        
    return count + 1
    

print(wc2("별 헤는 밤"))