from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self, number_bank, name, dateStart,dateEnd, sodu,bank,sodutb,state,suminday):
        self.__number_bank = number_bank
        self.__name = name
        self.__dateStart = dateStart
        self.__dateEnd = dateEnd
        self.__sodu = sodu
        self.__bank = bank
        self.__sodutb = sodutb
        self.__state = state
        self.__suminday = suminday

    @property
    def name(self):
        return self.__name
    @property
    def number_bank(self):
        return self.__number_bank
    @property
    def date_start(self):
        return self.__dateStart
    @property
    def date_end(self):
        return  self.__dateEnd
    @property
    def sodu(self):
        return self.__sodu
    @property
    def bank(self):
        return self.__bank
    @property
    def sodutb(self):
        return self.__sodutb
    @property
    def state(self):
        return self.__state
    @property
    def suminday(self):
        return self.__suminday



    def check_balance(self):
        if self.__state == 1:
            print(f"SO DU CUA TAI KHOAN {self.number_bank} LA: {self.sodu}")

    def chuyentien(self,other,money):
        if self.state == 1:
            if self.sodu - money > 70000:
                other.sodu += money
                self.sodu -= money
                self.suminday += money
                print("Chuyen tien thanh cong ")
            else:
                print("Loi khong du tien: ")
        else:
            print("Tai khoan da bi khoa")

    def naptien(self,money):
        if self.state == 1 and money > 0:
            self.__sodu += money
            print("Nap tien thanh cong ")
        else:
            print("Nap tien loi")

    @abstractmethod
    def ruttien(self,money,bank):
        if self.state == 1:
            if self.sodu - money > 70000 and money > 0:
                self.sodu -= money
                print("Rut tien thanh cong:")
                return 1
            else:
                print("So du loi")
        else:
            print("tai khoan cua ban bi khoa")

    def pay_bill(self, money, inter = False):
        if self.state == 1:
            if self.sodu - money > 70000 and money > 0:
                self.sodu -= money
                print("Thanh toan thanh cong:")
                return 1
            else:
                print("So du loi")
        else:
            print("tai khoan cua ban bi khoa")

    def saving(self, money):
        if self.state == 1:
            if self.sodu - money > 70000 and money > 0:
                self.sodu -= money
                print("Da gui tiet kiem: ")
            else:
                print("So du loi")
        else:
            print("tai khoan cua ban bi khoa")

    def lock(self):
        self.state = 0

    def unlock(self):
        self.tate = 1

    def __str__(self):
        return f"Name:{self.__name} | SO DU: {self.sodu} | Number_Bank: {self.__number_bank} | Bank: {self.bank}"\
                f"State: {self.state} | SumInDay: {self.suminday}"

    @sodu.setter
    def sodu(self, value):
        self.__sodu = value

    @suminday.setter
    def suminday(self, value):
        self.__suminday = value

    @state.setter
    def state(self, value):
        self.__state = value


class DomesticCard(Account):
    FEE_IN = 1100
    FEE_OUT = 3300


    def __init__(self, limit,number_bank, name, dateStart, dateEnd, sodu, bank, sodutb, state, suminday):
        super().__init__(number_bank,name,dateStart,dateEnd,sodu,bank,sodutb,state,suminday)
        self.limit = limit

    def ruttien(self,money,bank):
        result = super().ruttien(money,bank)
        if result > 0 and self.sodutb < 2000000:
            if self.bank == bank:
                self.sodu = self.sodu - DomesticCard.FEE_IN
            else:
                self.sodu = self.sodu - DomesticCard.FEE_OUT
    def chuyentien(self,other,money):
        if money < self.limit:
            super(DomesticCard,self).chuyentien(other,money)
        else:
            print("Loi vuot qua gioi han ")

    def __str__(self):
        return f"DomesticCar: Name:{self.name} | SO DU: {self.sodu} | Number_Bank: {self.number_bank} | Bank: {self.bank}" \
                f"State: {self.state} | SumInDay: {self.suminday} | Limit: {self.limit}"
class VisaCard(Account):
    FEE_IN = 0
    FEE_OUT = 9900
    FEE_FOREIN = 23900
    EXCHAGE = 23500

    def __init__(self,fee_year,id,tran_fee,limit_in_day, number_bank, name, dateStart, dateEnd, sodu, bank, sodutb, state, suminday):
        super().__init__(number_bank,name,dateStart,dateEnd,sodu,bank,sodutb,state,suminday)
        self.fee_year = fee_year
        self.id = id
        self.limit_in_day = limit_in_day
        self.transaction_fee = tran_fee

    def ruttien(self,money,bank):
        result = super().ruttien(money,bank)
        if result > 0 and self.sodutb < 5000000:
            if bank == self.bank:
                self.sodu -= 0
            if bank != self.bank:
                if self.is_domestic_bank(bank):
                    self.sodu -= VisaCard.FEE_OUT
                else:
                    self.sodu -= VisaCard.FEE_FOREIN

    def pay_bill(self, money, inter=False):
        """Khi thanh toán quốc tế thì trừ phí giao dịch quốc tế."""
        result = super().pay_bill(money)
        if inter is True and result > 0 and \
                self.sodu > self.sodu - 70000:
            self.sodu -= self.transaction_fee * VisaCard.EXCHAGE
        return result

    def chuyentien(self,other,money):
        if self.suminday < self.limit_in_day:
            super(VisaCard,self).chuyentien(other,money)
        else:
            print("Vuot qua muc giao dich ")

    def is_domestic_bank(self, bank):
        """Kiểm tra ngân hàng là trong nước hay nước ngoài. Dưới đây là
            một số ngân hàng làm ví dụ. Bạn tự bổ sung các ngân hàng khác.
        """
        match bank:
            case 'VCB' | 'MSB' | 'MB' | 'ACB' | 'ABBANK' | 'VietinBank' | \
                 'BIDV' | 'Techcombank' | 'Agribank' | 'OCB' | 'VIB' | 'SHB' | \
                 'SCB' | 'VPBank':
                return True
            case _:
                return False

    def __str__(self):
        return f"VisaCard Name:{self.name} | SO DU: {self.sodu} | Number_Bank: {self.number_bank} | Bank: {self.bank}" \
               f"State: {self.state} | SumInDay: {self.suminday} | Tranc: {self.transaction_fee} | Limit: {self.limit_in_day}"

def creat_fake_account():
    accounts = []
    accounts.append(DomesticCard(15000000,15102004,"NGUYEN DUC ANH","1/1/2023","1/1/2030",500000000,"MB",0,1,0))
 #   acc1 = Account(15102004,"NGUYEN DUC ANH","1/1/2023","1/1/2030",500000000,"MB",0,1,0)
    accounts.append(DomesticCard(15000000,18102005, "NGUYEN DUC NAM", "1/1/2023", "1/1/2030", 35000000, "VPBank", 0, 0, 0))
    accounts.append(DomesticCard(15000000,30092004, "NGUYEN HUONG LY", "1/1/2023", "1/1/2030", 150000000, "VIB", 0, 1, 0))
    accounts.append(VisaCard(50000,8788,2,20000000,1111000, "NGUYEN DUC ANH", "1/1/2023", "1/1/2030", 90000000, "MB-INTERNATIONAL", 0, 1, 0))
    accounts.append(VisaCard(50000,8888,2,20000000,2222000, "NGUYEN DUC ANH", "1/1/2023", "1/1/2030", 300000000, "VP-INTERNATIONAL", 0, 1, 0))
    accounts.append(VisaCard(50000,8889,2,20000000,8888000, "LE DUC MANH", "1/1/2023", "1/1/2030", 1500000, "MB", 0, 1, 0))
    return accounts

def print_acc(accounts):
    for i in accounts:
        print(i)
def checkbalance(accounts):
    num = int(input("Nhap stk : "))
    for i in accounts:
        if i.number_bank == num:
            i.check_balance()
def ruttienin(accounts):
    num = int(input("Nhap stk : "))
    money = int(input("Nhap so tien muon rut: "))
    for i in accounts:
        if i.number_bank == num:
            i.ruttien(money,i.bank)
            return None
    print("KHONG TIM THAY TAI KHOAN")
def napthe(accounts):
    num = int(input("Nhap stk: "))
    for i in accounts:
        if i.number_bank == num:
            money = int(input("Nhap so tien: "))
            i.naptien(money)
            return None
    print("Loi khong tim thay acc")
def paybill(accounts):
    numpy = int(input("Nhap stk: "))
    money = int(input("Nhap so tien muon thanh toan: "))
    for i in accounts:
        if i.number_bank == numpy:
            i.pay_bill(money)
            return None
    print("THAT BAI")

def paybillinter(accounts):
    numpy = int(input("Nhap stk: "))
    money = int(input("Nhap so tien muon thanh toan: "))
    for i in accounts:
        if i.number_bank == numpy and isinstance(i,DomesticCard) is False :
            i.pay_bill(money,True)
            return None
    print("THAT BAI")

def chuyentieninsame(accounts):
    chuyen = int(input("NHAP STK CHUYEN: "))
    for i in accounts:
        if i.number_bank == chuyen:
             nhan = int(input("NHAP STK NHAN: "))
             for j in accounts:
                if j.number_bank == nhan and j.number_bank != chuyen:
                    money = int(input("Nhap so tien muon chuyen "))
                    i.chuyentien(j,money)
                    return None
    print("That bai")



accounts = creat_fake_account()
menu = 0
while menu != 10:
    menu = int(input("Nhap chuc nang "))
    if menu == 1:
        print_acc(accounts)
    if menu == 2:
        print("Kiem tra so du: ")
        checkbalance(accounts)
    if menu == 3:
        napthe(accounts)
    if menu == 4:
        print("RUT TIEN NOI NGAN HANG")
        ruttienin(accounts)
    if menu == 5:
        print("THANH TOAN HOA DON NOI DIA")
        paybill(accounts)
    if menu == 6:
        print("THANH TOAN HOA DON QUOC TE")
        paybillinter(accounts)
    if menu == 7:
        print("CHUYEN TIEN NOI DIA CUNG NGAN HANG")
        chuyentieninsame(accounts)





