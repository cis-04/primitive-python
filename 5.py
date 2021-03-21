from random import*
size = ["XS", "S", "M", "L", "XL", "XXL"]
shirt_size = []
for i in range(1,11):
    shirt_size.append(choice(size))

def calculator():
    zeropocket = [0,0,0,0,0,0]
    for shirt in shirt_size:
        if shirt == "XS":
            zeropocket[0] += 1
        elif shirt == "S":
            zeropocket[1] += 1
        elif shirt == "M":
            zeropocket[2] += 1
        elif shirt == "L":
            zeropocket[3] += 1
        elif shirt == "XL":
            zeropocket[4] += 1
        elif shirt == "XXL":
            zeropocket[5] += 1
    return zeropocket
print(calculator())