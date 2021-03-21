def solution(arr):
    l_arr = list(arr)
    n = len(arr)
    for i in range(n):
        if l_arr[i] == "a":
            l_arr[i] = "z"
        elif l_arr[i] == "z":
            l_arr[i] = "a"
    return "".join(l_arr)
print(solution("abcz"))
