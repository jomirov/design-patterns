import math
#6
x = 3
y = 4
z = 5

a = (1 + math.sin((x - y)**2)) / (2 + z / abs(x-(1+y**2)))
b = math.cos(math.atan((1/z)**2))

print("6)",a)
print(b)
#7
x = 5
y = 3
z = 17
a = math.log(abs(y-math.sqrt(abs(x))),math.e)
b = x - x**2/math.factorial(3) + x**5/math.factorial(5)

print("7)",a)
print(b)
#8
x = 7
y = 4
z = 8
a = abs(math.sin(3*x + y + 15*z)) / (math.sqrt(12*(x**3) + 6*(y**2) + z**3) + x**2)
b = math.tan(7*(x**2) + math.e**(3*y))

print("8)",a)
print(b)
#9
x = 17
y = 16
z = 15
a = math.sqrt((abs(math.sin(8*y)) + 17 * x) / (1 - math.sin(4*y)*math.cos(z**2)))
b = math.sqrt(3*(z**2)/(3+math.tan(3*x)-math.sin(5*y)))

print("9)",a)
print(b)
#10
x = 6
y = 7
z = 8
a = x**(2*y) + (3*math.acosh(y**3)/(z**2 + x*y))
b = (abs(x-y)**2)/3*z+math.cos(x**2)

print("10)",a)
print(b)
#11
x = 3
y = 4
z = 5
a = 10 * math.log((x**y - math.sqrt(math.cosh(2))),math.e)
b = 2 * (x**2) + abs(y**2 - 3 * z)/math.e**(3*x - y)
print("11)",a)
print(b)
#12
x = 4
y = 5
z = 6
print("12)",a)
print(b)
a = (math.cos(x**2)+5*math.sin((x-y)**3)) / math.log((2*z + y**3),math.e)
b = (math.asinh((4*(x**2) + 5*(y**3)) / math.sqrt(3*z + x**2))) / math.log(7*x, math.e)
#13
x = 5
y = 6
z = 7
a = math.tan((x+y)**2 - math.sqrt(math.cosh(z**2)/math.tanh(z**2)))
b = math.log((x**2 + (math.e**(-3*y) / math.sin(y**3))),math.e)
print("13)",a)
print(b)
#14
x = 8
y = 9
z = 10
a = (y/math.sin(x) + (y/math.sin(x**2) - 3 * math.cos(z))) * math.e**(5*x)
b = (5-math.e**(z-2)) / (y+(x**2)*z**2 - (x**2) * math.tanh(z))
print("14)",a)
print(b)
#15
x = 9
y = 10
z = 11
a = abs(y**2 + 1) + y/(math.sin(z) - math.e**(z + 5))
b = math.sqrt((x - math.cos((y+z)**2)) / 5 + (math.log((abs(y-5*x)),math.e)) / math.sqrt(7))
print("15)",a)
print(b)