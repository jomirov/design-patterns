import math
x = 2
y = 6
z = 7

a = ((abs(x - 1)**(1/2)) - abs(y)**(1/3)) / (1 + (x**2/2) + (z**2/4))
b = (x*math.atan(z)+x*math.e**(-y - 3))
print("1)", a)
print(b)
#2
x = 5
y = 1
z = 4
a = (3 + math.e**(y - 1)) / (1 + x*y - x*math.tan(z))
b = abs(y - x) + ((y - x)**2)/2 + (abs(y - z)**2)/3

print("2)", a)
print(b)
#3
x = 1
y = 12
z = 6
a = (x + y/(x**2 + 4)) / (math.e**(x - 2) + 1 / (z**2 + 4))
b = (1 + math.cos(y - 2))/(x ** 4 + (math.sin(z ** 2)))
print("3)", a)
print(b)
#4
x = 11
y = 5
z = 10
a = x/(z**2 + x**2 / (y + x**3/3) )
b = 1 + math.sin(x) * math.tan(y**2) + math.sin(x) * 3.5
print("4)", a)
print(b)
#5
x = 15
y = 7
z = 3
a = (2 * math.cos(x - math.pi/4)) / (0.5 + math.sin(y ** 2))
b = 1 + z**2/(3 + z**2/5)

print("5)", a)
print(b)


#if else
a = 10
b = 5
c = 7
max = a
if b > max:
    max = b
if c > max:
    max = c
print("if else a,b,c -",10,5,7 )
print("max =",max)
