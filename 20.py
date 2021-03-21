def solution(arr, k):
    answer = 0
    thelist = []
    for i in arr:
        for b in i:
            thelist.append(b)
    thelist.sort()
    answer = thelist[k-1]
    return answer
arr = [[1,2,3],[4,5,6]]
print(solution(arr, 3))