numberpocket = [1,2,3,4,5,6,7,8,9,10]
def solution(numberpocket):
    output = 0
    for i in numberpocket:
        output += i
    number = 0
    for i in numberpocket:
        if i < (output / len(numberpocket)):
            number += 1
    return number
print(solution(numberpocket))