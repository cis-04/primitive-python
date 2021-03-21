def func(month, day):
    monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(month - 1):
        total += monthlist[i]
    total += day
    return total - 1
print(func(9, 25))

