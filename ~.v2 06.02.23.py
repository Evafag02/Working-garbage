# def A(n):
#     if n != 1: A(n-1)
#     print(n)
# A(int(input()))
def B(a, b):
    if a < b:
        B(a, b - 1)
        print(b)
    elif a > b:
        print(a)
        B(a - 1, b)
a = int(input())
b = int(input())
B(a, b)

