def solution(height, k):
    number = 0
    for h in height:
        if h > k:
            number += 1
    return number
print(solution([1,2,3,4,5], 3))