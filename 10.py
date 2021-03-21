def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1, len(characters)):
        if characters[i] != characters[i-1]:
            result += characters[i]
    return result

print(solution("dddddddddddaaaaaaaaaaaayyyyyyyyyyyyy"))