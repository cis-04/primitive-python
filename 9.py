def solution(arr):
    str = ''
    for i in sentence:
        if arr != ' ' and arr != ',':
            str += i
    size = len(str)
    for i in range(size//2):
        if str[i] != str[size -1 -i]:
            return False
    return True