TheValue = list(range(1,11))
n = 0
for i in range(len(TheValue)+1):
    n += i
normal = n / len(TheValue)
print("""
            총 합 : {}
            평균값 : {}
                            """.format(n,normal))
