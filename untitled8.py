import random

com1 = random.randrange(0,10)

while True :
    com2 = random.randrange(0,10)
    if com1 != com2:
        break
while True :
    com3 = random.randrange(0,10)
    if com1 != com2 and com2 != com3:
        break
        
while True:
    ball = 0
    strike = 0
    
    UserInput = input('숫자 3개 입력 : ')
    A = int(UserInput[0:1])
    B = int(UserInput[1:2])
    C = int(UserInput[2:3])

    if A == com1:
        strike += 1
    if B == com2:
        strike += 1
    if C == com3:
        strike += 1
        
    if A != com1 and A == com2:
        ball += 1
    if A != com1 and A == com3:
        ball += 1
    if B != com2 and B == com1:
        ball += 1
    if B != com2 and B == com3:
        ball += 1
    if C != com3 and C == com1:
        ball += 1
    if C != com3 and C == com2:
        ball += 1
    print("Strike : [", strike, '], Ball : [', ball, ']' )
    
    if strike == 3:
        break
        
