def gugudan2(fir, end):
    for i in range(fir, end + 1):
        
        print(str(i) + "단")
        for j in range(1, 10):
            
            print(str(i), "×", j, "=", int(i) * j)
        
        print("--------------------")
            
            
gugudan2(2, 6)