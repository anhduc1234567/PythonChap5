class Triangle:
    def __init__(self,a =  0,b = 0 ,c = 0):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        result = Triangle()
        result.a = self.a + other.a
        result.b = self.b + other.b
        result.c = self.c + other.c
        return result

    def __sub__(self, other):
        result = Triangle()
        result.a = self.a - other.a
        result.b = self.b - other.b
        result.c = self.c - other.c
        return result
    def chuvi(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Do dai lan luot cua tam giac la: {self.a} {self.b} {self.c}"

tri1 = Triangle(3, 4, 5)
tri2 = Triangle(5, 6, 7)
print(tri1 - tri2)
