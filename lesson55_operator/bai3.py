class Matrix:
    def __init__(self,row = 0,col = 0, data =None):
        if data is None:
            data = list()
        self.row = row
        self.col = col
        self.matrix = data

    def __add__(self, other):
        if self.row == other.row and self.col == other.col:
            result = []
            for i in range(0,self.row):
                result.append([])
                for j in range(0, self.col):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])

            return Matrix(self.row,self.col,result)
        else:
            print("LOI ")
            return None
    def __sub__(self, other):
        if self.row == other.row and self.col == other.col:
            result = []
            for i in range(0,self.row):
                result.append([])
                for j in range(0, self.col):
                    result[i].append(self.matrix[i][j] - other.matrix[i][j])

            return Matrix(self.row,self.col,result)
        else:
            print("LOI ")
            return None
    def __mul__(self, other):
        if self.col == other.row:
            result = []
            for i in range(0, self.row):
                result.append([])
                for j in range(0,other.col):
                    result[i].append(0)
                for x in range(0,other.col):
                    for y in range(0,self.col):
                        result[i][x] = result[i][x] + (self.matrix[i][y] * other.matrix[y][x])
            return Matrix(self.row,other.col,result)
        print("LOI")
    def __eq__(self, other):
        if self.row != other.row and self.col != other.col:
            return False
        for i in range(0,self.row):
            for j in range(0,self.col):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __str__(self):
        matrix = f'[row={self.row}, col={self.col}]\n'
        for row in self.matrix:
            for element in row:
                matrix += f'{element:<5}'
            matrix += '\n'
        return matrix

def addMatrix(row):
    data = []
    for i in range(0,row):
        data.append([int(x) for x in input().split()])
    return data

row = 4
col = 1
print("Nhap matrix 1: ")
data = addMatrix(row)
matrix1 = Matrix(row,col,data)
print("Nhap matrix 2: ")
matrix2 = Matrix(1,5,addMatrix(1))
print(matrix1 * matrix2)









