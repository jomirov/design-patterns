#1
a = 3
b = 2
print("1) 3 + 2 =", a+b)


#2
a = 5
print("2)")
if a % 2 == 0:
    print(a, " - саны жұп сан")
else:
    print(a, " - саны тақ сан")

#3
a = 5
b = 4
c = 7
print("3) максимал сан: ",max([a,b,c]))


#4
print("4)")
string = "abcdef"
num = 0
for i in string:
    num += 1
print(string, "сөзінде", num, "әріп бар")


#5
n = 10
sum = 0
for i in range(10):
    sum += i
print("5)",n," дейінгі сандар қосындысы: ", sum)


#6
string = "abcdef"
newString = ""
for i in range(1,len(string)+1):
    newString += string[-i]
print("6)",string,"кері түрде: ",newString)


#7
a = [1,2,53,64,234]
print("7)",a," тізімдегі кішісі:",min(a))


#8
a = [1,6,8,3,2,4,7]
print("8) сұрыпталған: ",sorted(a))



#9
a = 13
isJai = False
for i in range(2,a):
    if a % i != 0 or not a < 0:
        print(i,"true")
        isJai = True
    elif a % i == 0 or a < 0:
        print(i,"false")
        isJai = False
        break

if isJai == True:
    print(a,"jai san")
else:
    print(a,"jai san emes")


#10
a = "123 123 123"
b = a.split()
print("10) Сөздер саны: ",len(b))


#11
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

import numpy
newMatrix = numpy.transpose(matrix)

print("11)")
for i in newMatrix:
    print(i)
