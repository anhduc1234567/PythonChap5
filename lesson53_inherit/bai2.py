class Person:
    def __init__(self, Name, address, birth, CCCD ):
        self.name = Name
        self. address = address
        self.birth = birth
        self.cccd = CCCD
    def eat(self):
        print(f"{self.name} is eating ")
    def play(self):
        pass
    def work(self):
        pass
    def sleep(self):
        pass
class Student(Person):
    def __init__(self, ids,gpa,major,name, address, birth, CCCD):
        super().__init__(name,address,birth,CCCD)
        self.id = ids
        self.gpa = gpa
        self.major = major
    def homework(self):
        pass
    def exam(self):
        pass
    def fee(self):
        pass
class StudentPass(Student):
    def __init__(self,ids,gpa,major,name, address, birth, CCCD, salary, namratrg, xeploai):
        super().__init__(ids,gpa,major,name,address,birth,CCCD)
        self.salary = salary
        self.namratr =namratrg
        self.xeploai = xeploai
    def work(self):
        pass
    def recive(self):
        pass
class StudentNotPass(Student):
    def __init__(self,ids,gpa,major,name, address, birth, CCCD, namhoc, somonF):
        super().__init__(ids,gpa,major,name,address,birth,CCCD)
        self.somonF = somonF
        self.namhoc = namhoc

    def studyAgain(self):
        pass
    def dangkyhoc(self):
        pass
    def intern(self):
        pass
class Teacher(Person):
    def __init__(self, idt,hocvi,salary,major,name, address, birth, CCCD):
        super().__init__(name,address,birth,CCCD)
        self.id = idt
        self.hocvi = hocvi
        self.salary = salary
        self.major = major
    def teach(self):
        pass
    def chambai(self):
        pass
    def rade(self):
        pass
    def linhluong(self):
        pass