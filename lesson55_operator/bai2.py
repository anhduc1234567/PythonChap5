import math
class Fraction:
    def __init__(self, tuso = 1,mauso = 1 ):
        self.tuso = tuso
        self.mauso = mauso
    def simply(self):
        ucl = math.gcd(self.mauso,self.tuso)
        self.mauso = self.mauso // ucl
        self.tuso = self.tuso // ucl
    def __add__(self, other):
        result = Fraction()
        result.tuso = self.tuso * other.mauso + self.mauso * other.tuso
        result.mauso = self.mauso * other.mauso
        result.simply()
        return result

    def __sub__(self, other):
        result = Fraction()
        result.tuso = self.tuso * other.mauso - self.mauso * other.tuso
        result.mauso = self.mauso * other.mauso
        result.simply()
        return result

    def __mul__(self, other):
        result = Fraction()
        result.tuso = self.tuso * other.tuso
        result.mauso = self.mauso * other.mauso
        result.simply()
        return result

    def __truediv__(self, other):
        result = Fraction()
        if self.mauso != 0 and other.mauso != 0:
            result.tuso = self.tuso * other.mauso
            result.mauso = self.mauso * other.tuso
            result.simply()
            return result
        else:
            print("Khong the chia cho 0")
            return None

    def __eq__(self, other):
        if isinstance(other,Fraction):
            other.simply()
            self.simply()
            if self.mauso == other.mauso and self.tuso == other.tuso:
                return True
        return False

    def __ne__(self, other):
        if isinstance(other,Fraction):
            other.simply()
            self.simply()
            if self.mauso != other.mauso or self.tuso != other.tuso:
                return True
        return False

    def __gt__(self, other):
        other.simply()
        self.simply()
        return (self.tuso / self.mauso) > \
            (other.tuso / other.mauso)

    def __lt__(self, other):
        other.simply()
        self.simply()
        return (self.tuso / self.mauso) < \
            (other.tuso / other.mauso)

    def __ge__(self, other):
        other.simply()
        self.simply()
        return (self.tuso / self.mauso) >= \
            (other.tuso / other.mauso)

    def __le__(self, other):
        other.simply()
        self.simply()
        return (self.tuso / self.mauso) <= \
            (other.tuso / other.mauso)

    def __str__(self):
        return f"{self.tuso}/{self.mauso}"
f1 = Fraction(1,2)
f2 = Fraction(1,8)
print(f1 < f2)
