def solution(arr):
    jump = 0
    current = 0
    while current < len(arr):
        current += arr[current]
        jump += 1
    return jump
print(solution([1,2,3,4,5,6,7,8,9]))