print("input start/finish number")
a = int(input("start number:"))
b = int(input("finish number:"))

def SummingMachine(a,b):
    output = 0
    for i in range(a,b+1):
        output += i
    return output
print(SummingMachine(a,b))
