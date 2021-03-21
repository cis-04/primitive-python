MoodToday = input("오늘의 기분은 어떠신가요?----")
SchoolStudy = int(input("오늘 하루 학과 공부를 한 시간은 몆 시간 인가요?----"))
CodingToday = int(input("오늘 하루 코딩을 한 시간은 몆 시간 인가요?----"))
TiredToday = input("졸린가요? [y,n]----")
HungryToday = input("배고픈가요? [y,n]----")

print("기분이 {}인 만큼 열심히 하세요.".format(MoodToday))
if SchoolStudy < 1:
    print("무조건 학과공부를 하세요!!!")
elif SchoolStudy < 3:
    if CodingToday < 1:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 코딩을 2시간 이상 하세요.")
    elif CodingToday < 3:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 코딩을 1시간 이상 하세요.")
    elif CodingToday < 5:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다.")
    elif CodingToday < 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹으세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다. 코딩을 굳이 더 할 필요는 없읍니다.")
    elif CodingToday >= 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요. 코딩을 자제하세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹으세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다. 코딩을 자제하세요.")
elif SchoolStudy <= 5:
    if CodingToday < 1:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 코딩을 2시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 코딩을 쭉 하세요.")
    elif CodingToday < 3:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 코딩을 1시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 코딩을 쭉 하세요.")
    elif CodingToday < 5:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다.")
    elif CodingToday < 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹으세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다. 코딩을 굳이 더 할 필요는 없읍니다.")
    elif CodingToday >= 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹고 자세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("학과 공부를 3시간 이상 한 후, 밥을 먹고 자세요. 코딩을 자제하세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("학과 공부를 2시간 이상 한 후, 밥을 먹으세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다. 코딩을 자제하세요.")
elif SchoolStudy >= 5:
    if CodingToday < 1:
        if TiredToday == "y":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 2시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 2시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 2시간 이상 하세요.")
    elif CodingToday < 3:
        if TiredToday == "y":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 1시간 이상 한 후, 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 1시간 이상 한 후, 밥을 먹으세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 코딩을 1시간 이상 하세요.")
    elif CodingToday < 5:
        if TiredToday == "y":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹으세요.")
            elif HungryToday == "n":
                print("오늘은 이제 쉬세요.")
    elif CodingToday < 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹으세요. 오늘은 코딩을 굳이 더 할 필요는 없읍니다.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 하는 날입니다. 코딩을 굳이 더 할 필요는 없읍니다.")
    elif CodingToday >= 7:
        if TiredToday == "y":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹고 자세요. 코딩을 자제하세요.")
        elif TiredToday == "n":
            if HungryToday == "y":
                print("오늘은 학과 공부를 굳이 더 할 필요는 없읍니다. 밥을 먹으세요. 코딩을 자제하세요.")
            elif HungryToday == "n":
                print("오늘은 쉬세요")

