# A
# [print(i) for i in range(1, int(input())+1)]
# B
# a = int(input()); b = int(input())
# if a < b: [print(i, end=' ') for i in range(a, b + 1)]
# elif a > b: [print(i, end=' ') for i in range(a, b - 1, -1)]
# C
# n = int(input()); i = 1
# while i < n:
#     i = i * 2
# if i == n: print("YES")
# else: print("NO")
# D
# print(sum([int(i) for i in input()]))
# E
# [print(i, end=' ') for i in reversed((input()))]
# F
# [print(i, end=' ') for i in input()]
# G
# l = []; k = int(input())
# for i in range(k): l += [i] * i
# print(l[:int(input())])
# H
a = int(input()); b = int(input())
while a != 0 and b != 0:
    if a > b: a = a % b
    else: b = b % a
print(a + b)

#2 A
# s1 = input(); s2 = input()
# a = list(set(s1) & set(s2))
# for i in a: print(i, end=' ')

