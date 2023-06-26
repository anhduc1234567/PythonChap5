import math
from ulis1 import tichCacPhanSo,tongCacPhanSo,creatFraction
menu = 0
fractions = []
while menu != 10:
    print("Vui long chon chuc nang ")
    menu = int(input())
    if menu == 1:
        fractions.append(creatFraction())
    if menu == 2:
        for i in fractions:
            i.show_fractioc()
    if menu == 3:
        f = creatFraction()
        f.simply()
        print(f)
    if menu == 4:
        f1 = creatFraction()
        f2 = creatFraction()
        f3 = f1.add(f2)
        f3.simply()
        print(f"Tong cua f1 va f2 la : {f3}")
    if menu == 5:
       f_sum = tongCacPhanSo(fractions)
       print(f_sum)
    if menu == 6:
        f_sub = creatFraction()
        f_sub2 = creatFraction()
        f_result = f_sub.sub(f_sub2)
        print(f_result)
    if menu == 7:
        f_mul = creatFraction()
        f_mul2 = creatFraction()
        f_mul_result = f_mul.mul(f_mul2)
        print(f_mul_result)
    if menu == 8:
        f_devi = creatFraction()
        f_divi2 = creatFraction()
        f_divi_ressult = f_devi.divi(f_divi2)
        print(f_divi_ressult)
    if menu == 9:
        f_tich = tichCacPhanSo(fractions)
        print(f_tich)
