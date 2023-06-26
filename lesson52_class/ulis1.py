from Fraction import Fraction
def creatFraction():
    stra,strb = input("Nhap tu so va mau so ").split()
    if int(strb) != 0:
        print("them thanh cong ")
        return Fraction(tuso = int(stra), mauso = int(strb))
    else:
        return None
def tongCacPhanSo(arr):
    f = Fraction(0,1)
    for i in arr:
        f = f.add(i)
    f.simply()
    return f
def tichCacPhanSo(arr):
    f = Fraction(1,1)
    for i in arr:
        f = f.mul(i)
    f.simply()
    return f
