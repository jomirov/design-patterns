class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def x(self,x):
        print(x)
    def y(self,y):
        print(y)

    def move(self,x1,y1):
        self.x += x1
        self.y += y1

#A
print("A) ")
point = Point(3, 5)
print(point.x, point.y)
print()

#B
print("B) ")
point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
print()

#C
print("C) ")
class RedButton:
    count_click = 0
    def click(self):
        print("Тревога!")
        self.count_click += 1
    def count(self):
        return self.count_click
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())

#D
print("D) ")
class Programmer:
    whole_hours = 0
    pay = 0
    multi = 0

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def work(self, hours):
        self.whole_hours += hours
        if self.rank == "Junior":
            self.multi = 10
            self.pay += self.multi * hours
        elif self.rank == "Middle":
            self.pay += self.multi * hours
        elif self.rank == "Senior":
            self.pay += self.multi * hours

    def info(self):
        return f"{self.name} {self.whole_hours}ч. {self.pay}тгр."

    def rise(self):
        if self.rank == "Junior":
            self.rank = "Middle"
            self.multi = 15
        elif self.rank == "Middle":
            self.rank = "Senior"
            self.multi = 20
        elif self.rank == "Senior":
            self.multi += 1

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())

#E
print("E)")
class Rectangle:
    def __init__(self, a: tuple, b: tuple):
        self.x1 = a[0]
        self.y1 = a[1]
        self.x2 = b[0]
        self.y2 = b[1]

        self.uz = abs(self.x2 - self.x1)
        self.en = abs(self.y2 - self.y1)
    #E
    def perimeter(self):
        return 2 * (self.uz + self.en)

    def area(self):
        return self.uz * self.en
    #F
    def get_pos(self):
        return (self.x1, self.y1)

    def get_size(self):
        return (self.uz, self.en)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def resize(self, width, height):
        #height = y2 - y1
        self.x2 = width + self.x1
        self.y2 = height + self.y1
        self.uz = width
        self.en = height
    #G
    def turn(self):
        self.x1 *= (-1)
        self.y1 *= (-1)
    def scale(self, multiplier):
        self.x1 *= multiplier
        self.y1 *= multiplier
        self.x2 *= multiplier
        self.y2 *= multiplier

        self.uz *= multiplier
        self.en *= multiplier

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
print(rect.area())

#F
print("F)")
print("Move coords")
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
print("Resize")
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())


#G
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')



#H
class Checkers:
    shashki = {
        'H':['X','W','X','X','X','B','X','B'],
        'G':['W','X','W','X','X','X','B','X'],
        'F':['X','W','X','X','X','B','X','B'],
        'E':['W','X','W','X','X','X','B','X'],
        'D':['X','W','X','X','X','B','X','B'],
        'C':['W','X','W','X','X','X','B','X'],
        'B':['X','W','X','X','X','B','X','B'],
        'A':['W','X','W','X','X','X','B','X'],
    }
    def get_cell(self, cell):

        col = cell[0]
        row = int(cell[1])-1
        return self.shashki[col][row]
    def move(self, cell1, cell2):

        p1Col = cell1[0]
        p1Row = int(cell1[1]) - 1

        p2Col = cell2[0]
        p2Row = int(cell2[1]) - 1

        self.shashki[p2Col][p2Row] = self.shashki[p1Col][p1Row]
        self.shashki[p1Col][p1Row] = 'X'

checkers = Checkers()
checkers.move('G3', 'F4')
checkers.move('H6', 'G5')
for row in '87654321':
    print()
    for col in 'HGFEDCBA':
        print(checkers.get_cell(col+row), end='')



#I
print("I)")
class Queue:
    queue = []
    def push(self, item):
        self.item = item
        self.queue.append(item)
    def pop(self):
        popping_item = self.queue[0]
        self.queue.pop(0)
        return popping_item
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")

#J
print("\nJ)")
class Queue:
    queue = []
    def push(self, item):
        self.item = item
        self.queue.append(item)
    def pop(self):
        popping_item = self.queue[-1]
        self.queue.pop(-1)
        return popping_item
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")