#1)
s = [0, 1, 2, 3, 4, 5]
#1
print(s[2])
#2
print(s[:2])
#3
print(s[2:])
#4
print(s[:-2])
#5
print(s[4:])
#6
print(s[::-1])

print("")


#2)
c = [0, 1, 2, 3, 4, 5]
#1
c = [-2] + c
c = [-1] + c
print(c)
#2
c.append(0.1)
c.append(0.2)
print(c)

print("")


#3)
s = [0, 1, 2, 3, 4, 5]
#1
print(len(s))
#2
print(max(s))
#3
print(s*2)
for i in s:
    s[i] = i*2
print(s)
#4
s = [0, 1, 2, 3, 4, 5]
s.pop(1)
print(s)
#5
s = list(range(0,100))
print(s)

print()


#4)
p = [1,2,3,6,4,5,4]
#1
p.sort()
p.reverse()
print(p)
#2
print(len(p))

print()

#5)
p = [66, 25, 35, 4, 5, 156, 51, 4.5]
#1
p.insert(2,-2)
print(p)
#2
print(4.5 in p)