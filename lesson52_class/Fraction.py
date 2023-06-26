import math
class Fraction:

    def __init__(self, tuso = 1,mauso = 1 ):
        self.tuso = tuso
        self.mauso = mauso

    def add(self, other):
        result = Fraction()
        result.tuso = self.tuso * other.mauso + self.mauso * other.tuso
        result.mauso = self.mauso * other.mauso
        return result

    def sub(self, other):
        result = Fraction()
        result.tuso = self.tuso * other.mauso - self.mauso * other.tuso
        result.mauso = self.mauso * other.mauso
        result.simply()
        return result

    def mul(self,other):
        result = Fraction()
        result.tuso = self.tuso * other.tuso
        result.mauso = self.mauso * other.mauso
        result.simply()
        return result

    def divi(self,other):
        result = Fraction()
        if self.mauso != 0 and other.mauso != 0:
            result.tuso = self.tuso * other.mauso
            result.mauso = self.mauso * other.tuso
            result.simply()
            return result
        else:
            print("Khong the chia cho 0")
            return None

    def simply(self):
        ucl = math.gcd(self.mauso,self.tuso)
        self.mauso = self.mauso // ucl
        self.tuso = self.tuso // ucl
    def show_fractioc(self):
        print(f"{self.tuso} / {self.mauso}")
    def __str__(self):
        return f"{self.tuso} / {self.mauso}"
