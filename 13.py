# def solution(arr):
#     arr.sort()
#     group = []
#     for i in arr:
#         if i != arr[0] and i != arr[-1]:
#             group.append(i)
#     sum_group = sum(group)
#     return sum_group
# arri = [1, 2, 3, 4, 5]
# print(solution(arri))

def solution(arr):
    arr.sort()
    return sum(arr) - arr[0] - arr[-1]
arri = [1,2,3,4,5]
print(solution(arri))