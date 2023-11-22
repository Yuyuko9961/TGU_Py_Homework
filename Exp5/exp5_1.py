# 定义学校成员基类
class SchoolMember:
    def __init__(self, name, gender, age) -> None:
        self.name = name
        self.gender = gender
        self.age = age

    def get(self) -> None:
        print(f"姓名: {self.name}, 性别: {self.gender}, 年龄: {self.age}")

# 定义学生子类
class Student(SchoolMember):
    def __init__(self, name, gender, age, _class, sID, score) -> None:
        super().__init__(name, gender, age)
        self._class = _class
        self.sID = sID
        self.score = score

    def printInfo(self) -> None:
        self.get()
        print(f"班级: {self._class}, 学号: {self.sID}, 分数: {self.score}", end="\n\n")

# 定义教师子类
class Teacher(SchoolMember):
    def __init__(self, name, gender, age, department, tID, wages) -> None:
        super().__init__(name, gender, age)
        self.department = department
        self.tID = tID
        self.wages = wages

    def printInfo(self) -> None:
        self.get()
        print(f"科室: {self.department}, 工号: {self.tID}, 工资: {self.wages}", end="\n\n")


teacher1 = Teacher("tname1", "M", 25, "CS", "0024", 7500)
teacher2 = Teacher("tname2", "F", 33, "Math", "0032", 8500)
student1 = Student("sname1", "F", 18, 3, "2211640101", 100)
student2 = Student("sname2", "M", 20, 4, "2211640103", 80)

teacher1.printInfo()
teacher2.printInfo()
student1.printInfo()
student2.printInfo()
