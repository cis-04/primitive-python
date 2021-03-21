def pricecheck(grade, price):
    value = 0
    if grade == "S":
        value = price*0.95
    elif grade == "G":
        value = price*0.9
    elif grade == "V":
        value = price*0.85
    return value
print(pricecheck("V", 100))
