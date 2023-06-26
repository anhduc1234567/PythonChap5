class Person:
    def __init__(self, Name, address,email, birth, CCCD ):
        self.name = Name
        self. address = address
        self.birth = birth
        self.cccd = CCCD
        self.email = email
    def eat(self):
        print(f"{self.name} is eating ")
    def play(self):
        pass
    def work(self):
        pass
    def sleep(self):
        pass
    def info(self):
        print("I am person ")
class Student(Person):
    def __init__(self, ids,gpa,major,name, address,email, birth, CCCD):
        super().__init__(name,address,email,birth,CCCD)
        self.id = ids
        self.gpa = gpa
        self.major = major
    def homework(self):
        pass
    def exam(self):
        pass
    def fee(self):
        pass
    def info(self):
        print("i am Student")
class StudentPass(Student):
    def __init__(self,ids,gpa,major,name, address,email, birth, CCCD, salary, namratrg, xeploai):
        super().__init__(ids,gpa,major,name,address,email,birth,CCCD)
        self.salary = salary
        self.namratr =namratrg
        self.xeploai = xeploai
    def work(self):
        pass
    def recive(self):
        pass
    def info(self):
        print("i am graduate student")
class StudentNotPass(Student):
    def __init__(self,ids,gpa,major,name, address,email, birth, CCCD, namhoc, somonF):
        super().__init__(ids,gpa,major,name,address,email,birth,CCCD)
        self.somonF = somonF
        self.namhoc = namhoc

    def studyAgain(self):
        pass
    def dangkyhoc(self):
        pass
    def intern(self):
        pass
class Teacher(Person):
    def __init__(self, idt,hocvi,salary,major,name, address,email ,birth, CCCD):
        super().__init__(name,address,email,birth,CCCD)
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
    def info(self):
        print("i am teacher")

duc = Person("duc", "Hanoi","ducanh@gmail.com","15/10/2004",220222001)
ducanh = Student("SV001",4.5,"ai","duc", "Hanoi","ducanh@gmail.com","15/10/2004",220222001)
ducTuan = StudentPass("SV002",4.5,"ai","duc", "Hanoi","ducanh@gmail.com","15/10/2004",220222001,20020000,5,"gioi")
ducNam = StudentNotPass("SV002",4.5,"ai","duc", "Hanoi","ducanh@gmail.com","15/10/2004",220222001,2017,0)

duc.info()
ducanh.info()
ducTuan.info()
ducNam.info()