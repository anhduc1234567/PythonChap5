class Employee:
    AUTO_ID =1000
    def __init__(self,name,email,num_phone,salary):
        self.name = name
        self.email = email
        self.num_phone = num_phone
        self.salary = salary
        self.id = f"NV{Employee.AUTO_ID}"
        Employee.AUTO_ID += 1

    def checkin(self):
        pass
    def checkout(self):
        pass
    def work(self):
        pass
    def calculate_salary(self, working_day):
        real_salary = working_day / 22 * self.salary
        return real_salary

    def __str__(self):
        return f'{self.id:<12} {self.name:30}' \
               f'{self.email:30} {self.num_phone:15} {self.salary:<12}'
class Manager(Employee):
    def __init__(self,role,term,quater_salary,name,email,num_phone,salary ):
        super().__init__(name,email,num_phone,salary)
        self.role = role
        self.term = term
        self.quater_salary = quater_salary

    def dihop(self):
        pass
    def kyduyen(self):
        pass

    def calculate_salary(self, working_day):
        return super().calculate_salary(working_day) + \
            0.8 * self.quater_salary

    def __str__(self):
        return f'{super().__str__()}{self.term:12}{self.role:20}{self.quater_salary:12}'
class Developer(Employee):
    def __init__(self, role, num_language, num_project, kpi, name, email, num_phone, salary):
        super().__init__(name,email,num_phone,salary)
        self.role = role
        self.num_language = num_language
        self.num_project = num_project
        self.kpi = kpi

    def receive_task(self, task):
        print(f"Lập trình viên {self.name} đã nhận task {task}.")

    def solve(self, task):
        print(f"Lập trình viên {self.name} đang thực hiện task {task}.")

    def fix(self, task):
        print(f"Lập trình viên {self.name} đang fix bugs task {task}.")

    def report(self, task, manager):
        print(f"Lập trình viên {self.name} "
              f"đang làm báo cáo task {task} "
              f"cho quản lý {manager.full_name}.")

    def calculate_salary(self, working_day):
        base_salary = super().calculate_salary(working_day)
        bonus = base_salary * 0.3 / 100 * self.kpi
        return base_salary + bonus

    def __str__(self):
        return f'{super().__str__()}{self.role:20} {self.num_language:<12}' \
               f'{self.num_project}  {self.kpi}'
class Tester(Employee):
    def __init__(self,role,tool,num_bug,num_testcase,name, email, num_phone, salary):
        super().__init__(name,email,num_phone,salary)
        self.role = role
        self.tool = tool
        self.num_bug =num_bug
        self.num_testcase = num_testcase

    def calculate_salary(self, working_day):
        base_salary = super().calculate_salary(working_day)
        bonus = base_salary * 0.2 / 100 * self.num_testcase + 50 * self.num_bug
        return base_salary + bonus

    def __str__(self):
        return f'{super().__str__()}{self.role}  {self.tool}' \
               f'{self.num_bug}  {self.num_testcase}'
class Task:
    ID_AUTO = 100
    def __init__(self,name,time):
        self.id = Task.ID_AUTO
        self.name = name
        self.time = time
        Task.ID_AUTO += 1
    def __str__(self):
        return f"Cong viec: {self.name} mat khoang : {self.time} de hoan thành"
class Table:
    ID_AUTO = 100
    def __init__(self,nhanvien,task,start,end,result):
        self.nhanvien = nhanvien
        self.task = task
        self.start = start
        self.end = end
        self.result = result
        self.id = Table.ID_AUTO
        Table.ID_AUTO += 1
    def __str__(self):
        return f"{self.nhanvien.name}  {self.task.name}   {self.start}  {self.end} {self.result}"
class TableSalary:
    ID_AUTO = 100
    def __init__(self,nhanvien, sum_task,num_task_complete,num_task_uncomplete,tienphat,luongthuclinh,songaylamviec):
        self.id = TableSalary.ID_AUTO
        self.nhanvien = nhanvien
        self.task = sum_task
        self.num_task_complete = num_task_complete
        self.num_task_uncomplete = num_task_uncomplete
        self.tienphat = tienphat
        self.salary = luongthuclinh
        self.daywork = songaylamviec


    def __str__(self): # 12.1f: làm tròn đến 1 chữ số sau phần thập phân
        return f'{self.id:<12} {self.nhanvien.name:20}'\
               f'{self.task} {self.daywork}'\
               f'{self.num_task_complete} {self.num_task_uncomplete}'\
               f'{self.tienphat} {self.salary}'

def creat_employ():
    employee = []
    employee.append(Employee("NGUYEN DUC ANH","abc@gmail.com",8401938838,30000000))
    employee.append(Manager("Giam doc","MAKERING",30000000,"NGUYEN DUC NAH","DUCANH@GMAIL.ENDU",19293383929,100020200))
    employee.append(Tester("TEST","JAVA",3,10,"NGUYEN DUC NAH","DUWCNINWCI@GMAIL.COM",889398398,10000000))
    employee.append(Developer("LAP TRINH",3,3,4,"Nguyen duc anh","ducanh@gmail.com",92847292,9111122329))
    return employee
def print_em(em):
    for i in em:
        print(i)
employee = creat_employ()
print_em(employee)
