def solution(price, money):   #price = 구매한 물건들 
    sum_all = sum(price)      #money = 지불한 돈의 양
    if money > sum_all:
        return money - sum_all
    else:
        return -1