#1
# a = str(input('введите строку: '))
#
#
# def answer(a):
#     return a == a[::-1]
#
#
# print(answer(a))

#2
# n = int(input('Введите число: '))
# dict = {'a': 30, 'b': 40, 'c': 50}
# a = dict.values()
# if n in a:
#     print('YES')
# else:
#     print('NO')


#3
# x = float(input())
# def f(x):
#     if -2 < x < 5:
#         n = 5 * (x ** 2) + 6
#         print('При: ', x, 'значение f(x): ', n)
#     if x >= 5:
#         k = x ** 3 + 7
#         print('При: ', x, 'значение f(x): ', k)
# f(x)


#4
# a = list(range(1, 31))
# b = 0
# for i in a:
#     a[b] = i ** 2
#     b += 1
# print(a)

#5
# n = 1
# y = 2
# z = 3
# x = float(input())
# x2 = x
# x3 = 2
# s = (y/z)*x
# for i in range(9):
#     y += 1
#     z += 1
#     x = x2 ** x3
#     x3 += 1
#     n = (y / z) * x
#     s += n
# print(s)


# 6,7
# s = 1
# n = 1
# for i in range(7):
#     n /= 2
#     s += n
#     print(n)
# print(s)


# 8
# n = int(input())
# sum = 0
# for k in range(1,n):
#     a = (k**2)/(k+2)
#     sum += a
# print(sum)

# 9
# x = 4
# y = 3
# sum = y / x
# for i in range(6):
#     x += 1
#     y += 2
#     sum += x / y
# print(sum)

# 10
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# res = [x + y for x in list1 for y in list2]
# print(res)

# 11
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)

# 12
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')

# 13
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res_dict = dict(zip(keys, values))
# print(res_dict)
#

# 14
# def average(list):
#     return sum(list)/len(list)
#
# a = list(range(20))
# print(average(a))

# 15
# def unique_list(l):
#     x = []
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x
#
# print(unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5]))

# 16
# s = str(bin(int(input("Введите число от 0 до 255: "))))[2:].rjust(8, "0")
# print(s)

# 17
# def test_prime(n):
#     if (n == 1):
#         return False
#     elif (n == 2):
#         return True
#     else:
#         for x in range(2, n):
#             if (n % x == 0):
#                 return False
#         return True
#
# print(test_prime(37))


# 18
# def longestLength(a):
#     max1 = len(a[0])
#     temp = a[0]
#
#     for i in a:
#         if (len(i) > max1):
#             max1 = len(i)
#             temp = i
#
#     print("The word with the longest length is:", temp,
#           " and length is ", max1)
#
#
# a = ["one", "two", "third", "four"]
# longestLength(a)


# 19
# def isEven(n):
#     return (n % 2 == 0)
# n = 101
# print("Even" if isEven(n) else "Odd")


# 20
# def BFrequency(my_list):
#     freq = {}
#     for item in my_list:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1
#
#     for key, value in freq.items():
#         print("% d : % d" % (key, value))
#
# my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# BFrequency(my_list)
