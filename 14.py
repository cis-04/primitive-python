def solution(arr):
    arr.sort()
    firstmostbiggest = arr[-1]
    arr2 = []
    for i in arr:
        if i != arr[-1]:
            arr2.append(i)
    arr2.sort()
    secondmostbiggest = arr2[-1]
    return firstmostbiggest - secondmostbiggest
print(solution([1,2,3,4,5,6]))