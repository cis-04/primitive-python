from random import*
print("야구게임 입니다.")
print(" 각기 다른 세 정수를 입력하세요.")
try:
    FirstNumber = input("첫 번째 숫자를 입력하세요")
    SecondNumber = input("두 번째 숫자를 입력하세요")
    ThirdNumber = input("세 번째 숫자를 입력하세요")
    int(FirstNumber)
    int(SecondNumber)
    int(ThirdNumber)
    print("{0}, {1}, {2} 을(를) 입력하셨습니다.".format(FirstNumber,SecondNumber,ThirdNumber))
    if FirstNumber == SecondNumber or SecondNumber == ThirdNumber or ThirdNumber == FirstNumber:
        print()
        print()
        print("세 정수가 모두 달라야 합니다!")
except:
    print("정수를 입력하세요!")
group = [int(FirstNumber), int(SecondNumber), int(ThirdNumber)]
# club = [1,2,3,4,5,6,7,8,9]
# a = choice(club)
# b = choice(club)
# c = choice(club)



# if b == a or b == c:
#     b = choice(club)
# if b == a or b == c:
#     b = choice(club)
# if b == a or b == c:
#     b = choice(club)
# if b == a or b == c:
#     b = choice(club)
# if c == a or c == b:
#     c = choice(club)
# if c == a or c == b:
#     c = choice(club)
# if c == a or c == b:
#     c = choice(club)
# if c == a or c == b:
#     c = choice(club)
# if c == a or c == b:
#     c = choice(club)

a,b,c = 2,6,9

def note(a,b,c):
    output = 0
    for i in group:
        if i == a:
            output += 1
        elif i == b:
            output += 1
        elif i == c:
            output += 1
        else:
            pass
    return output

output = note(a,b,c)

if output == 0:
    print("세 수가 모두 같지 않습니다.")
elif output == 1:
    print("하나의 수가 같습니다.")
elif output == 2:
    print("두 수가 같습니다.")
else:
    print("세 수가 모두 같습니다.")






