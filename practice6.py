h, m = map(int, input().split())
h = int(h)
m = int(m)

if m < 45:
    m = 60 + m - 45
    if h == 0:
        h = 23
    else:
        h = h - 1
elif m >= 45:
    m = m - 45
print(h, m)