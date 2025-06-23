a = int(input('숫자 입력 : '))
x = 0
for i in range (2,a,1):
    if a%i == 0:
        x=1
if x == 0:
    print(a,'은(는) 소수입니다.')
else:
    print(a,'은(는) 소수가 아닙니다.')
    
        