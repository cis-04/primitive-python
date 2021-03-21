def solution(n, m):
    sum_n = 0
    sum_m = 0
    for i in range(1, n):
        sum_n += i
    for i in range(1, m + 1):
        sum_m += i
    return sum_m - sum_n
print(solution(1, 5))