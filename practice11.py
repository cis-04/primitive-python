numbers = int(input())
for i in range(numbers):
    x, y = map(int, input().split())
    print("Case #{0}: {1} + {2} =".format(i + 1, x, y), x + y)