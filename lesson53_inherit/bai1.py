class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(f"Toa do tam la : ({self.x}, {self.y})")
    def chuvi(self):
        return 0
    def dientich(self):
        return 0

class Circle(Shape):

    def __init__(self,r,x,y):
        super().__init__(x,y)
        self.r = r
    def chuvi(self):
        return 3.14 * 2 * self.r
    def dientich(self):
        return  3.14 * self.r * self.r

class hinhchunhat(Shape):
    def __init__(self, lenght, width, x, y):
        super().__init__(x,y)
        self.length = lenght
        self.width = width
    def chuvi(self):
        return (self.length + self.width) * 2
    def dientich(self):
        return (self.length * self.width)
class Triagle(Shape):
    def __int__(self, a, b, c, x, y):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

h = hinhchunhat(3,4,1,1)
c = Circle(3,1,1)
print(h.chuvi(), h.dientich())
print(c.chuvi(), c.dientich())