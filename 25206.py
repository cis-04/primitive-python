sum = 0
scoresum = 0
for i in range(20):
    subName,score,alpha = map(str,input().split())
    score = float(score)
    if alpha != 'P':
        scoresum += score
    if alpha[0] == 'A':
        if alpha[1] == '+':
            sum += 4.5*score
        else: sum += 4.0*score
    if alpha[0] == 'B':
        if alpha[1] == '+':
            sum += 3.5*score
        else: sum += 3.0*score
    if alpha[0] == 'C':
        if alpha[1] == '+':
            sum += 2.5*score
        else: sum += 2.0*score
    if alpha[0] == 'D':
        if alpha[1] == '+':
            sum += 1.5*score
        else: sum += 1.0*score
print(sum/scoresum)