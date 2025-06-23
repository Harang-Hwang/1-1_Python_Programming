a = input('컴퓨터 활용 자격증 유무(Y/N)?')

if a == 'Y' :
    b = int(input('몇 학년?'))
    if b == 4:
        print('응시 지원 대상자임')
    else :
        print('응시 지원 자격 미충족')
else:
    print('응시 지원 자격 미충족')