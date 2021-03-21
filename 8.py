def solution(arr):
    count = 0
    for i in arr:
        if 680 <= i < 800:
            count += 1
    return count
arr = [590, 489, 695, 738, 800, 908]
print(solution(arr))