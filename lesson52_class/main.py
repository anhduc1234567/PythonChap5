from Classed import Classed
from Student import Student
from Table_mark import Table_matk
from Subject import Subject

def add_subject(arr):
    id = input("Nhap ma mon hoc : ")
    name = input("Nhap ten mon hoc: ")
    sotin = int(input("So tin: "))
    sotiet = int(input("So tiet: "))
    sotest = int(input("So test: "))
    sub = Subject(id,name,sotin,sotiet,sotest)
    arr.append(sub)
def add_student(arr):
    id = input("Nhap ma sinh vien: ")
    name = input("Nhap ho va ten: ")
    add = input("Nhap dia chi: ")
    email = '22022661@vnu.edu.vn'
    gioitinh = input("Gioi tinh: ")
    khoa = input("Khoa: ")
    student = Student(id,name,add,email,gioitinh,khoa)
def find_subject(sub,key):
    for i in sub:
        if i.id == key:
            return i
    return None
def find_student(sub,key):
    for i in sub:
        if i.ids == key:
            return i
    return None
def find_class(sub,key):
    for i in sub:
        if i.idc == key:
            return i
    return None

def add_classes(arr,subjects):
    if len(subjects) > 0:
        idc = input("Nhap ma lop: ")
        name = input("Nhap ten: ")
        phong = input("Nhap phong: ")
        time = input("Nhap time: ")
        subjects_id = input("Nhap ma mon hoc: ")
        sub = find_subject(subjects,subjects_id)
        if sub is not None:
            cla = Classed(idc,name,phong,time,sub)
            arr.append(cla)
def print_subject(sub:Subject):
    print(f"ID: {sub.id} | Name: {sub.name_sub} | TinChi: {sub.sotin} - {sub.sotiet} - {sub.sotest}")
def print_student(stu:Student):
    print(f"ID: {stu.ids} Ho: {stu.ho} Dem: {stu.mid_name} Ten: {stu.name} | Diachi: {stu.address}"
          f" |  Gioi tinh: {stu.gioitinh} | Email: {stu.email} | Khoa: {stu.khoa} ")
def print_classed(clas:Classed):
    print(f"ID: {clas.idc} Name: {clas.name_class} Subject: {clas.sub.name_sub} Time:{clas.time} Room: {clas.phong}")
def print_table_mark(tab:Table_matk):
    print(f"{tab.ids} - {tab.sinhvien.name} - {tab.gpa} - {tab.capacity}" )
def print_subjects(sub):
    for i in sub:
        print_subject(i)
def print_students(stu):
    for i in stu:
        print_student(i)
def print_classes(cla):
    for i in cla:
        print_classed(i)
def print_mark_class(idc,classes):
    a = Classed()
    for i in classes:
        if i.idc == idc:
            a = i
    for j in a.danh_sach_diem:
        print_table_mark(j)

def add_table_mark(classed,students):
    idc = input("Nhap ma lop hoc")
    c = find_class(classed,idc)
    if c is not None:
        ids = input("Nhap ma sinh vien: ")
        s = find_student(students,ids)
        if s is not None:
            hc1 = float(input("Nhap diem he so 1: "))
            hc2 = float(input("Nhap diem he so 2: "))
            hc3 = float(input("Nhap diem he so 3: "))
            table = Table_matk(ids,s,hc1,hc2,hc3)
            c.danh_sach_diem.append(table)
            print("THEM THANH CONG")
def create_fake_subjects():
    subjects = [Subject('SJ1000', 'Java', 3, 45, 4),
                Subject('SJ1001', 'C++', 3, 46, 5),
                Subject('SJ1002', 'C#', 4, 60, 5),
                Subject('SJ1003', 'NodeJS', 3, 45, 4),
                Subject('SJ1004', 'Android Java', 4, 60, 5),
                Subject('SJ1005', 'ASP.NET', 4, 60, 5),
                Subject('SJ1006', 'SQL', 3, 45, 5)]
    return subjects
def create_fake_students():
    """This method create and return fake students."""
    students = [Student('SV100', 'Long Văn Hoang','Hà Nội', 'longhoangshark@xmail.com',  'Nam', 'CNTT'),
                Student('SV103', 'Nguyen Oanh Hồng','Hồ Chí Minh', 'hongoanhunin@xmail.com',  'Nữ', 'CNTT'),
                Student('SV104', 'Pham Thị Hồng Nhung', 'Hà Nội', 'hongnhungcute@xmail.com', 'Nữ', 'HTTT'),
                Student('SV105', 'Le Thi Hồng', 'Thái Bình','hongnhunglele@xmail.com',  'Nữ', 'HTTT')]
    return students
def create_fake_couses(subjects):
    """This method create and return fake courses."""
    courses = [Classed('C100', 'Java 1', 'A2-205', '14-16h', subjects[0]),
               Classed('C101', 'Java 2', 'A2-205', '16-18h', subjects[0]),
               Classed('C102', 'Android 1', 'A2-201', '10-12h', subjects[4]),
               Classed('C103', 'Android 2', 'A2-105', '14-16h', subjects[4])]
    return courses

menu = 0
subjects = create_fake_subjects()
students = create_fake_students()
classes = create_fake_couses(subjects)
while menu != 14:
    menu = int(input("Nhap chuc nang: "))
    if menu == 1:
        add_subject(subjects)
    if menu  == 2:
        print("Them 1 sv vao danh sach: ")
        add_student(students)
    if menu == 3:
        add_classes(classes,subjects)
    if menu == 4:
        print("----------DANH SACH MON HOC LA-----------")
        print_subjects(subjects)
    if menu == 5:
        print('--------DANH SACH SINH VIEN LA------------')
        print_students(students)
    if menu == 6:
        print("---------DANH SACH LOP HOC LA-------------------------")
        print_classes(classes)
    if menu == 7:
        print("--------Nhap diem sinh vien trong tung lop hoc them ma lop-----")
        add_table_mark(classes,students)
    if menu == 8:
        idc = input("Nhap id cua lop de xem diem: ")
        print(f'Diem cua lop {idc}')
        print_mark_class(idc,classes)


