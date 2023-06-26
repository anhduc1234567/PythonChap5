import datetime


class FullName:
    """Lớp mô tả thông tin họ và tên đầy đủ."""
    def __init__(self, fname):
        self.__first_name = ''
        self.__mid_name = ''
        self.__last_name = ''
        self.set_full_name(fname)

    def set_full_name(self, fname):
        words = fname.split()
        self.__first_name = words[len(words) - 1]
        self.__last_name = words[0]
        for i in range(1, len(words) - 1):
            self.__mid_name += words[i] + ' '

    @property
    def first_name(self):
        return self.__first_name

    @property
    def mid_name(self):
        return self.__mid_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.__last_name} {self.__mid_name}{self.__first_name}'
class Person:

    def __init__(self,full_name,CCCD,birth):
        self.__full_name = FullName(full_name)
        self.__id = CCCD
        self.__birth = birth
    @property
    def full_name(self):
        return self.__full_name
    @property
    def id(self):
        return self.__id
    @property
    def birth(self):
        return self.__birth

    def __str__(self):
        return f'Name: {self.__full_name} ID: {self.__id:10} '\
                f'Birth: {self.__birth:15}'

    def work(self):
        pass
class Student(Person):
    AutoId = 1000

    def __init__(self,gpa,major,full_name,CCCD,birth):
        super().__init__(full_name,CCCD,birth)
        self.__msv = f'SV{Student.AutoId}'
        self.__gpa = gpa
        self.__major = major
        Student.AutoId += 1

    @property
    def mvs(self):
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
        return f'{super().__str__()}{self.mvs:15}{self.gpa:<10}' \
               f'{self.major:15}'

class Subject:
    ID_SUB =1000
    def __init__(self,name,sotin):
        self.__name_subject = name
        self.__sotin = sotin
        self.__id_sub = Subject.ID_SUB
        Subject.ID_SUB += 1

    @property
    def name_subject(self):
        return self.__name_subject
    @property
    def sotin(self):
        return self.__sotin
    @name_subject.setter
    def name_subject(self,value):
        self.__name_subject = value
    @property
    def id_sub(self):
        return self.__id_sub

    def __str__(self):
        return f'{self.id_sub:<10}{self.name_subject:15}{self.sotin:<10}'
class Register:
    ID_REG = 100
    def __init__(self,sub =None,student =None):
        self.__id_register = Register.ID_REG
        self.__subject = sub
        self.__student = student
        self.__time = datetime.datetime.now()

    @property
    def id_register(self):
        return self.__id_register

    @property
    def subject(self):
        return self.__subject

    @property
    def time(self):
        return self.__time

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value
    def __eq__(self, other):
        return self.student.mvs == other.student.mvs and \
                self.subject.id_sub == other.subject.id_sub
    def __str__(self):
        date_str = f'{self.time.day:02}/{self.time.month:02}/' \
                   f'{self.time.year:4} {self.time.hour:02}:' \
                   f'{self.time.minute:02}:{self.time.second:02}'
        return f'{self.id_register}  {self.student.mvs}    ' \
               f'{self.student.full_name:}    ' \
               f'{self.subject.id_sub:<10}{self.subject.name_subject:15}  ' \
               f'{date_str:25}'
def creat_student():
    students = []
    students.append(Student(3.5,'QKTK','NGUYEN DUC ANH',22022661,'15/10/2004'))
    students.append(Student(4.0,'NN-ĐỨC','NGUYEN HUONG LY',300900192,'30/9/2004'))
    students.append(Student(3.4, 'QKDL', 'NGUYEN DUC NAM', 220223661, '15/10/2028'))
    students.append(Student(4.0, 'NN-ANH', 'NGUYEN HUONG LAM', 300900192, '30/9/2031'))
    return students
def creat_sub():
    subjects = []
    subjects.append(Subject('Triết hoc - Mác',4))
    subjects.append(Subject('Kinh tế chính trị', 3))
    subjects.append(Subject('Tiếng Đức', 5))
    subjects.append(Subject('Cơ sở dữ liệu', 3))
    return subjects
def creat_reg(student, sub):
    id = input("Nhap msv: ").upper()
    idsub = int(input("Nhap ma mon hoc: "))
    stu = None
    subject = None
    for i in student:
        if i.mvs == id:
            stu = i
            break
    for j in sub:
        if idsub == j.id_sub:
            subject = j
            break
    if stu is not None and subject is not None:
        return Register(subject,stu)
    else:
        print("Loi khong tim thay")
        return None
def is_register_exist(mregisters, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in mregisters:
        if item == r:
            return True
    return False
def show_student(students):
    print('==> Danh sách sinh viên:')
    print(f'{"CMND/CC":10}{"Họ và tên":25}{"Ngày sinh":12}'
          f'{"Mã SV":10}{"Điểm TB":10}{"C.Ngành":15}')
    for e in students:
        print(e)
def find_by_msv(reg,student):
    msv = input("Nhap msv ").upper()
    print("Danh sach mon hoc ma sv dang ky la: ")
    for i in reg:
        if i.student.mvs == msv:
            print(i)
def show_reg(re):
    for i in re:
        print(i)
def show_subject(subject):
    for i in subject:
        print(i)

def count_reg(sub,reg):
    count = 0
    for i in reg:
        if i.subject.id_sub == sub.id_sub:
            count += 1
    return count
def static(sub,reg):
    for i in sub:
        print(f"ID:{i.id_sub} {i.name_subject} so luot dang ky: {count_reg(i,reg)}")
menu = 0
students = creat_student()
subject = creat_sub()
register = []

while menu != 10:
    menu = int(input("Nhap chuc nang: "))
    if menu == 1:
        print("DANG KÝ MON HOC")
        reg = creat_reg(students,subject)
        if reg is not None:
            if is_register_exist(register,reg):
                print("DA TON TAI")
            else:
                print("DANG KÝ THÀNH CÔNG")
                register.append(reg)
    if menu == 4:
        students.sort(key=lambda x:(x.full_name.first_name,x.full_name.last_name))
    if menu == 5:
        show_student(students)
    if menu == 6:
        show_subject(subject)
    if menu == 7:
        show_reg(register)
    if menu == 8:
        find_by_msv(register,students)
    if menu == 9:
        print("==============THONG KE DANG KY MON HOC LA==============")
        static(subject,register)




