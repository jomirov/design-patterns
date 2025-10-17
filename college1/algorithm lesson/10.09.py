#2
a = 27
i = 2
while a % i != 0 or i < a:
    i += 1
print(f"2) Ең кішкентай бөлгіш {a} - {i}")

#3
a = 5 # tenge
print("3) Кәмпит бағасы: ", a)
for i in range(1,10):
    print(f"{i} кг бағасы: {i*5}")

#4
sum = 0
i = 0
while i < 10:
    sum += i
    i += 1
print(f"4) Сандар қосындысы: {sum}, сандар саны: {i}")

#5
a = 5
b = 15
sum = 0
for i in range(a,b):
    sum += i
print(f"5) {a} бастап {b} дейінгі сандар суммасы: {sum}")

#6
a = [-2,-5,-3,-4,10]
i = 0
sum = 0
while i < len(a):
    sum += a[i]
    i += 1
print(f"6) {a} арифметикалық орта - {sum/i}")

#7
a = 5
b = 15
sum = 0
for i in range(a,b):
    sum += i**2
print(f"7) {a} бастап {b} дейінгі сандар квадрат суммасы: {sum}")

#8
a = [2,3,4,5,6,7,8]
sum = 0
i = 0
while i < len(a):
    while a[i] % 2 == 0:
        sum += a[i]
        break
    i += 1

print(f"8) {a} бойынша жуп сан суммасы: {sum}")

#9
a = 95
sum = 0
count = 0
for i in range(a,200):
    sum += i
    count += 1
print(f"9) {a} бастап 200 ге дейінгі сандар arifmet orta: {sum/count}")

#10
a = [2,3,-2,-4,-2,7]
i = 0
count = 0
while i < len(a):
    while a[i] > 0:
        count += 1
        break
    i += 1
print(f"10) {a} тізбегі бойынша оң сандар саны: {count}")
#11
a = 7
b = 23
sum = 0
for i in range(a,b):
    sum += i
print(f"11) {a} бастап {b} дейінгі сандар қосындысы: {sum}")

#12
n = 128
k = 0

while n != 2**k:
    k += 1
print(f"12) {n} - 2-нің {k} дәрежесінде шығады")

#13
a = 23
sum = 0
for i in range(a,50):
    sum += i ** 2
print(f"13) {a} бастап 50 дейінгі квадратталған сандардың қосындысы: {sum}")

#14
n = 32
k = 1
while 5**k < n:
    k += 1
print(f"14) 5**{k}>{n}")

#15
a = [1,2,3,4,5,6,7,8,9,0]
sum = 0
count = 0
for i in a:
    sum += i
    count += 1
print(f"15) Тізбектегі сандардың қосындысы: {sum}, сандар саны: {count} ")
