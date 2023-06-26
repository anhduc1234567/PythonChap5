class FullName:
    def __init__(self, first, mid, last):
        self.__first = first
        self.__last = last
        self.__mid = mid

    @property
    def first_name(self):
        return self.__first

    @property
    def mid_name(self):
        return self.__mid

    @property
    def last_name(self):
        return self.__last

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Person:
    def __init__(self, pid, full_name, dob):
        self.__person_id = pid
        self.__full_name = full_name
        self.__birth_date = dob

    @property
    def person_id(self):
        return self.__person_id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def birth_date(self):
        return self.__birth_date

    def work(self, task):
        print(f'{self.full_name} is doing {task}.')

    def show_info(self):
        print(self)

    def __str__(self):
        return f'{self.person_id:15}  {self.full_name:25}' \
               f'{self.birth_date:12}'

class Student(Person):
    AutoId = 1000

    def __init__(self,gpa,major,full_name,CCCD,birth):
        super().__init__(CCCD,full_name,birth)
        self.__msv = f'SV{Student.AutoId}'
        self.__gpa = gpa
        self.__major = major
        Student.AutoId += 1

    @property
    def msv(self):
        return self.__msv
    @property
    def gpa(self):
        return self.__gpa
    @property
    def major(self):
        return self.__major

    def doexam(self,sub):
        pass
    def register(self,subject):
        pass

    def __str__(self):
        return f'{super().__str__()}{self.msv:15}{self.gpa:<10}' \
               f'{self.major:15}'

class Teacher(Person):
    ID_TEA = 1001
    def __init__(self,salary,chuyen_mon, pid, full_name, dob):
        super().__init__(pid,full_name,dob)
        self.__salary = salary
        self.__chuyen_mon = chuyen_mon
        self.__mgv = f"GV{Teacher.ID_TEA}"
        Teacher.ID_TEA += 1

    @property
    def salary(self):
        return self.__salary
    @property
    def chuyen_mon(self):
        return  self.__chuyen_mon
    @property
    def mgv(self):
        return self.__mgv
    def __str__(self):
        return f"GV:{super().__str__()} {self.__mgv} {self.__salary} {self.chuyen_mon}"

class Subject:
    ID_SUB =1000
    def __init__(self,name_subject,sotin):
        self.__name_subject = name_subject
        self.__sotin = sotin
        self.__id_sub = Subject.ID_SUB
        Subject.ID_SUB += 1

    @property
    def name_subject(self):
        return self.__name_subject
    @property
    def sotin(self):
        return self.__sotin
    @property
    def id_sub(self):
        return self.__id_sub

    def __str__(self):
        return f"ID:{self.id_sub}   {self.__name_subject}  {self.sotin}"

class Mark:
    ID_Auto = 100
    def __init__(self,student = None, gpa = 0.0):
        self.__student = student
        self.__id_mark = Mark.ID_Auto
        self.__gpa = gpa
        self.phanloai()
        Mark.ID_Auto += 1

    @property
    def student(self):
        return self.__student
    @property
    def id_mark(self):
        return self.__id_mark
    @property
    def gpa(self):
        return self.__gpa

    def phanloai(self):
        if self.gpa > 0:
            if self.gpa < 4.0:
                self.__capacity = "Yếu"
            elif 4.0 <= self.gpa < 6.5:
                self.__capacity = "Trung bình"
            elif 6.5<= self.gpa < 8:
                self.__capacity = "Khá"
            elif 8.0 <= self.gpa < 9:
                self.__capacity = "Gioi"
            else:
                self.__capacity = "Xuat xac"
    @property
    def capacity(self):
        return self.__capacity
    def __str__(self):
        return f"Bang diem {self.__id_mark} cua: {self.student.full_name} {self.gpa}  {self.capacity}"
class Class:
    ID_AUTO = 100
    def __init__(self,subject = None,teacher =None,room = 101):
        self.__id_class = Class.ID_AUTO
        self.__subject = subject
        self.__teacher = teacher
        self.__room = room
        self.__mark = []
        Class.ID_AUTO += 1

    @property
    def id_class(self):
        return self.__id_class
    @property
    def subject(self):
        return self.__subject
    @property
    def teacher(self):
        return  self.__teacher
    @property
    def room(self):
        return self.__room
    @property
    def mark(self):
        return self.__mark
    @mark.setter
    def mark(self,value):
        self.__mark.append(value)

    def __str__(self):
        return f'{self.id_class} {self.__teacher.full_name}  {self.subject.name_subject}'\
                f'{self.room}'

def creat_student():
    students = []
    students.append(Student(8.3,"TTNT","NGUYEN DUC ANH",30204003918,"15/10/2004"))
    students.append(Student(9.4, "NN-ĐỨC", "NGUYEN HUONG LY", 30104003009, "30/09/2004"))
    students.append(Student(7.3, "QTKD", "PHAM DUC CHIEN", 30204003918, "5/7/2004"))
    students.append(Student(8.3, "NN-ANH", "NGUYEN NGOC LINH", 30204000018, "1/4/2004"))
    students.append(Student(8.7, "QTKD", "LE TUAN NAM", 30104006818, "6/8/2004"))
    return students

def creat_teacher():
    teachers = []
    teachers.append(Teacher(30000000,"CNTT",1234567898,"TRAN TUAN NAM","2/2/1983"))
    teachers.append(Teacher(44000000,"NN-ĐỨC",1234567898,"LE THI UYEN","1/12/1973"))
    teachers.append(Teacher(50000000, "TTNT", 1234567898, "NGUYEN QUOC TUAN", "4/6/1980"))
    teachers.append(Teacher(30000000, "NN-ANH", 1234567898, "LE TRAN NAM", "2/9/1983"))
    return teachers

def creat_subject():
    subjects = []
    subjects.append(Subject('Triết hoc - Mác', 4))
    subjects.append(Subject('Kinh tế chính trị', 3))
    subjects.append(Subject('Tiếng Đức', 5))
    subjects.append(Subject('Cơ sở dữ liệu', 3))
    return subjects
def creat_class(classes,subjects,teacheres):
    idsub = int(input("Nhap ma mon hoc: "))
    idgv= input("Nhap ma giang vien: ")
    room = int(input("Nhap phong: "))
    subject  = None
    teacher = None
    for i in subjects:
        if i.id_sub == idsub:
            subject = i
            break
    for j in teacheres:
        if j.mgv == idgv:
            teacher = j
            break
    if subject is not None and teacher is not None:
        classes.append(Class(subject,teacher,room))
def find_student(student,msv):
    for i in student:
        if i.msv == msv:
            return i
    return None
def find_class(classes,idc):
    for i in classes:
        if i.id_class == idc:
            return i
    return None
def find_teacher(teacher,mgv):
    for i in teacher:
        if i.mgv == mgv:
            return i
    return None
def find_subject(sub,idsub):
    for i in sub:
        if i.id_sub == idsub:
            return i
    return None
def is_exist(mark,student):
    for i in mark:
        if i.student.msv == student.msv:
            return True
    return False
def add_mark(classes,students):
    idc = int(input("Nhap ma lớp: "))
    msv = input("Nhap ma msv: ")
    clas = find_class(classes,idc)
    student = find_student(students,msv)
    gpa = float(input("Nhap diem tb: "))
    if clas is not None and student is not  None:
        mark = Mark(student,gpa)
        if is_exist(clas.mark, student) is False:
            clas.mark.append(mark)
        else:
            print("DA TON TAI DIEM CUA SINH VIEN")
    else:
        print("Loi")
def print_list(list):
    for i in list:
        print(i)
classes =[]
students = creat_student()
subjects = creat_subject()
teachers = creat_teacher()
menu = 0
while menu != 10:
    menu = int(input("Nhap chuc nang: "))
    if menu == 1:
        print("Them danh sach diem vào lop: ")
        add_mark(classes,students)
    if menu == 2:
        print("Them class: ")
        creat_class(classes,subjects,teachers)
    if menu == 3:
        print("=====DANH SACH STUDENT LA:====")
        print_list(students)
    if menu == 4:
        print("======DANH SACH GIANG VIEN LA======")
        print_list(teachers)
    if menu == 5:
        print("=======DANH SACH CAC LOP HOC LA=========")
        print_list(classes)
    if menu == 6:
        print("========DANH SACH CAC MON HOC LA======")
        print_list(subjects)
    if menu == 7:
        print("DANH SACH BANG DIEM CUA SINH VIEN TRONG LOP")
        idc = int(input("Nhap ma lop: "))
        cla = find_class(classes,idc)
        if cla is not None:
             print_list(cla.mark)
        else:
            print("LOP KHONG TON TAI")
    if menu == 8:
        students.sort(key=lambda x:(x.gpa))














