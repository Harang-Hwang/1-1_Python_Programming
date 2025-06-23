a = input('이름 : ')
b = int(input('키(Cm) : '))
c = int(input('체중(Kg) : '))
d = c / (b/100)**2
if d < 20:
    x = '저체중'
elif 20<= d <=24:
    x = '정상'
elif 25 <= d <= 29:
    x = '과체중'
else:
    x = '비만'
    
print(f'{a}님의 BMI 결과는 키 : {b:0,.1f}cm, 체중 : {c:0,.1f}kg, BMI 지수 : {d:0,.2f}이며, 판정은',x,'이다.')