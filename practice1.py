from random import*

element1 = randrange(1,11)
element2 = randrange(1,11)
element3 = randrange(1,11)
element4 = randrange(1,11)
element5 = randrange(1,11)

thelist = [element1,element2,element3,element4,element5]
# print(thelist)
a = input("0에서 10 사이의 예상 숫자를 선택하시오 :")
a = float(a)

if a in thelist:
    print("win")
else:
    print("lose")