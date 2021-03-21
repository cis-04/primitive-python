try:
    scores = int(input("점수를 입력하세요."))
except:
    print("정수값을 입력하세요!")
else:
    if scores == 100:
        print("만점입니다!!!")
    elif scores >= 90:
        print("1등급 입니다!")
    elif scores >= 80:
        print("2등급 입니다!")
    elif scores >= 70:
        print("3등급 입니다!")
    else:
        print("망했습니다!!!")