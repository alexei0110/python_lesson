a = [[1, 2, 3, 4], [4, 3, 2, 1], [6, 7, 8, 9]]
b=  [[4, 3, 5, 8], [3, 5, 7, 9], [1, 2, 5, 8]]

class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))


    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

m1 = Matrix(a)
m2 = Matrix(b)

print(m1, '\n')
print(m2, '\n')
print(m1 + m2)
