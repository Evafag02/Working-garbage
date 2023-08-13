from math import *
import numpy as np
s = 0
for x in np.arange(0.1, 2.2, 0.2):
    y = x**2 - ((1+cos(x+1)*2)/2)
    s += y
print(s)

n = 10 #int(input("Введите число:"))
x = 5
s = 0
for i in range(1,n+1):
    f = x/sin(i*x)
    s += f
print(s)