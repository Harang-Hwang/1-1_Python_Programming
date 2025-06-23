i = 0
ii = 0
iii = 0


while True :
    i += 1
    a = int(input('어떤 수? '))
    if a%2 == 0:
        ii += 1
        print('입력한 수 ',a,'은(는) 짝수이다.')
    if a%2 != 0:
        iii += 1
        print('입력한 수 ',a,'은(는) 홀수이다.')
    if i == 3:
        print('홀수 게수 : ',iii)
        print('짝수 개수 : ', ii)
        break