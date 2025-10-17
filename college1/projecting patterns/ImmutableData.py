from dataclasses import dataclass
#1
@dataclass(frozen=True)
class UserProfile:
    name: str
    email: str
    role: str
    def showRole(self, new_role):
        return UserProfile(self.name, self.email, new_role)

user1 = UserProfile("Jandos","qwerty123@gmail.com","Reader")
print("#1")
print(f"Жаңа пайдаланушы: {user1}")
user2 = user1.showRole("Writer")
print(f"Өзгертілген пайдаланушы: {user2}")

print()

#2
@dataclass(frozen=True)
class Vector2D:
    shape: str
    length: float
    def add(self, add_num: float):
        new_length = self.length + add_num
        return Vector2D(self.shape,new_length)
    def scale(self, scale_num):
        new_length = self.length * scale_num
        return Vector2D(self.shape,new_length)

kvadrat = Vector2D("kvadrat",5)
print("#2")
print(f"Жаңа құрылған пішін: {kvadrat}")
kvadratV2 = kvadrat.add(3)
print(f"Өзгертілген пішін add method:{kvadratV2}")
kvadratV3 = kvadratV2.scale(2)
print(f"Өзгертілген пішін scale method:{kvadratV3}")

#3
@dataclass(frozen=True)
class FrozenInvoice:
    student_name: str
    exam_points: list
    def showPoints(self):
        return f"Студент: {self.student_name}\nЖалпы бағалары: {self.exam_points}\nОрташа бағасы: {sum(self.exam_points)/len(self.exam_points)}"

print()
print("#3")
student = FrozenInvoice("Arman",[90,85,80,90,95])
print(student.showPoints())


#comment