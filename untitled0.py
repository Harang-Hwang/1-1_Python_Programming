a = 0
for x in range(5):
    b = int(input('숫자 : '))
    
    if b != 3:
        print(b)
        a += b
        
print('합계 : ', a)
