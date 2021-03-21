try:
    R = int(input("정수를 입력하세요."))
except:
    print("정수를 입력하세요!")
else:
    if R % 4 == 0:
        print("{}를 4로 나누면 나누어 떨어진다.".format(R))
    elif R % 4 != 0:
        remain = R % 4
        print("{}를 4로 나누면 나머지는 {} 이다.".format(R,remain))