def solution(name_list):
    count = 0
    for name in name_list:
        for n in name:
            if n == "j" or n == "k":
                count += 1
                break
    return count
print(solution(["jack", "chuk", "dumm", "hollv"]))