class Employee:

    def __init__(self, id = "01", name = "", age = 0,\
                 address = "", number_phone = 0, salary = 0, exp = 0\
                 ):
        self.id = id
        self.age =age
        self.address = address
        self.number_phone = number_phone
        self.salary = salary
        self.exp = exp
        self.name = name
        self.setName(name)

    def setName(self, name):
        word = [x for x in name.split()]
        self.first_name = word[len(word) - 1]
        self.ho = word[0]
        dem = ""
        for i in range(1,len(word) -1):
            dem = dem + word[i] + " "
        self.mid_name = dem
def print_nv(e:Employee):
    print(f'ID: {e.id} |Ho: {e.ho}| Dem: {e.mid_name} |Name: {e.first_name} |Dia chi: {e.address} |Toi: {e.age} |Exp: {e.exp}| Luong: {e.salary}')
def add_employee(arr):
    id = input("Nhap id : ")
    name = input("Nhap ten: ")
    age = int(input("Nhap tuoi: "))
    address = input('Nhap dia chi: ')
    num = int(input("Nhap sdt: "))
    sal = int(input('Nhap luong:L '))
    exp = int(input("Nhap exp: "))
    e = Employee(id,name,age,address,num,sal,exp)
    print_nv(e)
    arr.append(e)
    print("ADD thanh cong")
def print_nvs(arr):
    print("Danh sach nhan vien la: ")
    for i in arr:
        print_nv(i)

def find_id(arr:list, ids):
    for i in arr:
        idf = i.id.lower()
        if idf == ids.lower():
            print_nv(i)
            return None
    print("Khong tim thay")
    return None

menu = 0
employee= []
e1 = Employee("NV001","Nguyen Minh Tuan", 13,"Thai Nguyen",int('0989171789'),10000000,3)
employee.append(e1)
e2 = Employee("NV002","Dao Manh Lan", 18,"Thai Binh",int('0968151789'),10500000,3)
employee.append(e2)
e3 = Employee("NV003","Dao Manh Anh", 18,"Thai Binh",int('0968151789'),20500000,3)
employee.append(e3)
while menu != 14:
    menu = int(input("Nhap chuc nang "))
    if menu == 1:
        add_employee(employee)
    if menu == 2:
        print_nvs(employee)
    if menu == 3:
        ids = input("Nhap ten nv can tim ")
        find_id(employee,ids)
    if menu == 4:
        iddel = input("Nhap id de xoa: ")
        for i in employee:
            if i.id == iddel:
                employee.remove(i)
        print("xoa thanh cong")
    if menu == 5:
        employee.sort(key = lambda x:x.salary, reverse= True)
        print_nvs(employee)
    if menu == 6:
        employee.sort(key = lambda name:name.first_name, reverse= False)
        print_nvs(employee)
    if menu == 7:
        print("Nhap ten nv: ")
        na = input()
        na.lower()
        for i in employee:
            n = i.first_name.lower()
            if n == na:
                print_nv(i)





