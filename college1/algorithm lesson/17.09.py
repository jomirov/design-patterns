#1
n = 21
num = 1 #1 5 10 16 23
add = 4
i = 0
while n > num:
    num += add + i
    i += 1
print(f"1) {num} - {n} саныннан үлкен")

#2
grades = [90, 80, 70, 95, 78, 83]
count = 0
sum = 0
for i in grades:
    count += 1
    sum += i
print(f"2) экзамен ораташа багасы: {sum/count}")

#3
a = 4
sequence = 1 + 1/2 #+1/3+1/4...
i = 1
while a > sequence:
    sequence += 1/i
    i += 1
print(f"3) 1+1/2+...+1/n n-нің {i} мәнінде {a} санынан үлкен")

#4
#r=r1+r2+...
rs = [20,40,20,70,100]
rsum = 0
for i in rs:
    rsum += i
print(f"4) электрлік тізбектегі жалпы кедергінің мәні {rsum}")

#5
grades = [80,70,77,88,99,100,65]
sum = 0
for i in grades:
    sum += i
print(f"5) группадағы оқушылар орта бағасы: {sum/len(grades)}")

#6
i = 0
print("6)")
while i < 21:
    print(f"2**{i} = {2**i}")
    i += 1

#7
oblast = [
    [5000,400], #people, area
    [7000,200],
    [8000,700],
    [6000,500],
    [8000,800],
    [9000,1000]
]
s = 0
p = 0
for raion in oblast:
    p += raion[0]
    s += raion[1]
print(f"7) плотность жителей в области: {p/s} человек/км2")

#8
podarok = 500 #tg
sum = 0
birthday = 0
while sum < 40000:
    podarok *= 2
    sum += podarok
    birthday += 1
print(f"8) {birthday} туған күнде {sum} жиналады")

#9
ameba = 1 #3 sagat = 2 ameba
time = [3,6,9,12,15,18,21,24]
for i in time:
    print(f"{i} сағат ішінде {2**(i/3)} амеба болады")

#10
xlist = [1,1.5,2,2.5,3]
x = 0
y = -0.5*x + x
print("10)")
for x in xlist:
    print(f"x = {x}, y = -0.5*x + x = {-0.5*x+x}")

#11
probeg = 10 #km + 10%
days = 7
print("11)")
for i in range(1,8):
    probeg += 0.1 * probeg
    print(f"11) {i} күні - {probeg}км")

#12
a = 325
sum = 0
multi = 1
i = 0
while i < len(str(a)):
    sum += int(str(a)[i])
    multi *= int(str(a)[i])
    i += 1
print(f"12) {a} сандарының қосындысы: {sum}, көбейтіндісі: {multi}")