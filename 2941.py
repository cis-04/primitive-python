# word = input()
# sum = len(word)
# for i in range(len(word)-1):
#     if word[i] == 'c':
#         if word[i+1] == '=' or word[i+1] == '-':
#             sum -= 1
#     elif word[i] == 'd':
#         if word[i+1] == '-':
#             sum -= 1
#         if i+3 > len(word):
#                 break
#         if word[i+1] == 'z' and word[i+2] == '=':
#             sum -= 2
#     elif word[i] == 'l' and word[i+1] == 'j':
#         sum -= 1
#     elif word[i] == 'n' and word[i+1] == 'j':
#         sum -= 1
#     elif word[i] == 's' and word[i+1] == '=':
#         sum -= 1
#     elif word[i] == 'z' and word[i+1] == '=':
#         if word[i-1] != 'd':
#             sum -= 1
# print(sum)

#완전 어렵게품..
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')
# print(len(word))