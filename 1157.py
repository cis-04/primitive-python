word = input()
li = [0]*91
for i in range(len(word)):
    num = ord(word[i])
    if ord(word[i]) <= 90:
        li[num] += 1
    else: li[num-32] += 1
max = 0
for i in range(len(li)):
    if li[i] > max:
        max = li[i]
if li.count(max) > 1:
    print('?')
else: print(chr(li.index(max)))