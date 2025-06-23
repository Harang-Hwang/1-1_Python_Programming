userList = []
def again():
    print("중복됩니다. 다시 입력해주세요")
    
while True :    
    userID = input("아이디 입력 : ")  
    if userID == "0" :
        break    
    if userID in userList :
        again()
        
        continue
    userList.append(userID)
    
print(userList)

