class Account:
    def __init__(self, number_bank = 0, name ="", tyoe='', sodu=0, namBank="viettin-bank", start='20/6/2023', end = '30/4/2030'):
        self.number_bank = number_bank
        self.name = name
        self.type = tyoe
        self.sodu = sodu
        self.nameBank = namBank
        self.dateStart = start
        self.dateEnd = end
def creatAcc(arr):
    num = int(input("Nhap so tai khoan: "))
    name = input("Nhap ten: ")
    type = input("TAIKHOANNGANHANG")
    sodu = 0
    nameB = input("Nhap ten tai khoan: ")
    s = "20/6/2023"
    e = "30/4/2030"
    acc = Account(num,name,type,sodu,nameB,s,e)
    arr.append(acc)
def print_acc(acc:Account):
    print(f'{acc.name} | {acc.number_bank} | {acc.sodu} |{ acc.type} | {acc.nameBank} | {acc.dateStart} -> {acc.dateEnd}')
def print_accs(arr):
    for i in arr:
        print_acc(arr.get(i))
def add(acc,stk,money):
    if acc.get(stk) is not None and money > 0:
        acc.get(stk).sodu = acc.get(stk).sodu + money
        print("SUcess")
    else:
        print("Loi")
def ruttien(acc,stk,money):
    if acc.get(stk) is not None and acc.get(stk).sodu > money:
        acc.get(stk).sodu = acc.get(stk).sodu - money
        print("Thanh cong")
    else:
        print("Loi")
def delete(acc:dict, key):
    acc.pop(key)
def trans(acc, stk_chuyen, stk_nhan, money):
    if acc.get(stk_chuyen) is not None and acc.get(stk_chuyen).sodu > money and acc.get(stk_nhan) is not None:
        add(acc,stk_nhan,money)
        ruttien(acc,stk_chuyen,money)
        print("Thanh cong")
    else:
        print("Loi")


accounts = dict()
acc1 = Account(1510,"NGUYEN DUC ANH","TAIKHOAN NGAN HANG",1000000,"MB-BANK")
acc2 = Account(3009,"NGUYEN HUONG LY","TAIKHOAN NGAN HANG",1500000,"TECHCOM-BANK")
acc3 = Account(1710,"NGUYEN THI NGA","TAIKHOAN NGAN HANG",2000000,"BIDV-BANK")
accounts[1510] = acc1
accounts[3009] = acc2
accounts[1710] = acc3
menu = 0
while menu != 9:
    menu = int(input("Nhap tuy chon: "))
    if menu == 1:
        print_accs(accounts)
    if menu == 2:
        stk = int(input("Nhap so tai khoan: "))
        money = int(input("Nhap so tien can nap : "))
        add(accounts,stk,money)
    if menu == 3:
       stk1 = int(input("Nhap so tai khoan chuyen: "))
       stk2  = int(input("Nhap so tai khoan nhan: "))
       money = int(input("Nhap so tien chuyen: "))
       trans(accounts,stk1,stk2,money)
    if menu == 4:
        stk_del = int(input("Nhap stk can xoa: "))
        delete(accounts,stk_del)

