class Classed:
    def __init__(self, idc = "", name_class = "", phong = "", time ="", sub = None, danh_sach_diem=None):
        if danh_sach_diem is None:
            self.danh_sach_diem = []
        self.idc = idc
        self.name_class = name_class
        self.phong = phong
        self.time = time
        self.sub = sub
        self.danh_sach_diem = []

