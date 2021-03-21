from random import*
GrandClub = list(range(-20,21))

theunits = []

def ClubSelector(Howmany = 20):
    for i in range(Howmany):
        theunits = choice(GrandClub)
        return theunits
       
output1 = map(ClubSelector, GrandClub)
RealClub = list(output1)
RealClub = list(filter(None, RealClub))
max = RealClub[-1]
for i in RealClub:
    if max < i:
        max = i
print("최댓값:", max)
print("리스트:", RealClub)
