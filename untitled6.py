i = 0
A = 0
while True :
    i += 1
    a = int(input('숫자 : '))
    if a%2 == 0:
        A += 1
    if i==5 :
        print('짝수 개수 : ',A,'게')
        break
    
    