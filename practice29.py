# class FourCal:
#     pass                       #pass 는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 이용한다.

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def min(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first // self.second
        return result

a = FourCal(4,2)
print(a.add())
print(a.mul())
print(a.min())
print(a.div())

#상속
# class 클래스 이름(상속할 클래스 이름)
# class MoreFourCal(FourCal):
#     pass
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.min())
print(a.div())
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):              #상속한 클래스에 있는 매서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩 이라고 한다.
        if self.second == 0:
            return 0
        else:
            return self.first // self.seond
a = SafeFourCal(2,0)
print(a.div())

#클래스 변수
class Family:
    lastname = "염"        #클래스 변수 ====> 모든 객제에 공유된다
print(Family.firstname)
a = Family()
print(a.firstname)