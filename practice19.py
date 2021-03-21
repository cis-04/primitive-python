#입력한 값들의 합을 구하는 함수

def SumAll(*a):
    output = 0
    for n in a:
        output += n
    return output
print(SumAll(1,2,3,4,6))