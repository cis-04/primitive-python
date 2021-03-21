def listmaker(arr):
    counter = [0 for _ in range(1001)]
    for i in arr:
        counter[i] += 1
    return counter

def max(arr):
    ret = 0
    for i in arr:
        if ret < i:
            ret = i
    return ret

def min(arr):
    ret = 1001
    for i in arr:
        if i != 0 and ret > i:
            ret = i
    return ret

def solution():
    counter = listmaker(arr)
    max_value = max(counter)
    min_value = min(counter)
    thevalue = max_value // min_value
    return thevalue

arr = [1,3,5,7,9]
print(solution())
