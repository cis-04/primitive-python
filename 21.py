def solution(shoes_size):
    answer = [0 for _ in range(len(shoes_size))]
    for i in shoes_size:
        if i == "7":
            answer[i] += 1
        elif i == "7.5":
            answer[i] += 1
        elif i == "8":
            answer[i] += 1
        elif i == "8.5":
            answer[i] += 1
        elif i == "9":
            answer[i] += 1
        elif i == "9.5":
            answer[i] += 1
    return answer