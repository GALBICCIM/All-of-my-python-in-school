def login(id, pw):
    if id == "hansei" and pw == "hansei1234":
        return True
    
    else:
        return False
    
    
print(login("hansei", "hansei1234"))