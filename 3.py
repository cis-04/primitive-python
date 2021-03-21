class discountmachine:
    def __init__(self, rank, price):
        self.rank = rank
        self.price = price
    def Sd(self, price):
        Sdiscount = price * 0.95
        return Sdiscount
    def Gd(self, price):
        Gdiscount = price * 0.90
        return Gdiscount
    def Vd(self, price):
        Vdiscount = price * 0.85
        return Vdiscount
    def discount(self, rank, price):
        if rank == "S":
            theprice = self.Sd(price)
        elif rank == "G":
            theprice = self.Gd(price)
        elif rank == "V":
            theprice = self.Vd(price)
        else:
            print("S,G,V 중 하나를 입력하세요")
        return theprice
therank = input("회원 등급을 입력하세요[S,G,V]=>")
theprice = int(input("가격을 입력하세요"))

theinput = discountmachine(therank, theprice)
print(theinput.discount(therank, theprice))