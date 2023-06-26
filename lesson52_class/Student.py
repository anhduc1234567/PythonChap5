class Student:
    def __init__(self, ids = "", name = "", address = "", email ="", gioitinh = "", khoa = ""):
        self.ids = ids
        self.address = address
        self.email = email
        self.gioitinh = gioitinh
        self.khoa = khoa
        self.setName(name)

    def setName(self, name):
        word = [x for x in name.split()]
        self.name = word[len(word) - 1]
        self.ho = word[0]
        dem = ""
        for i in range(1, len(word) - 1):
            dem = dem + word[i] + " "
        self.mid_name = dem

