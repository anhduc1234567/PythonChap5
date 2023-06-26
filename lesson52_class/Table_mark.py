class Table_matk:
    def __init__(self, ids = "", sinhvien = None, hs1 = 0.0,hs2 = 0.0,hs3 = 0.0):
        self.ids = ids
        self.sinhvien = sinhvien
        self.hs1 = hs1
        self.hs2 = hs2
        self.hs3 = hs3
        self.calculate_gpa()
        self.calculate_capacity()

    def calculate_gpa(self):
        self.gpa = 0.1 * self.hs1 + 0.2 * self.hs2 + 0.7 * self.hs3

    def calculate_capacity(self):
        if 9.0 <= self.gpa <= 10.0:
            self.capacity = "Xuất sắc"
        elif 8.0 <= self.gpa < 9.0:
            self.capacity = "Giỏi"
        elif 6.5 <= self.gpa < 8:
            self.capacity = "Khá"
        elif 5.0 <= self.gpa < 6.5:
            self.capacity = 'Trung bình'
        elif 4.0 <= self.gpa < 5.0:
            self.capacity = 'Trung bình yếu'
        else:
            self.capacity = 'Trượt môn'
