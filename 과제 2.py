won=input("환전하고 싶은 원화 : ")
us=input("1$ 당 ")
s=int(won)/int(us)
print("환전하고 싶은 원화 {0:,}".format(int(won)),
      "원은 US 달러로 $ {0:,.2f}이다.".format(s))
