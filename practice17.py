a = int(input("input number"))
def CalCulaTor(a):
    output = 1
    for i in range(1,a+1):
        output*=i
    return output
print(CalCulaTor(a))
#7자리 입력하면 컴 터짐
#6또한