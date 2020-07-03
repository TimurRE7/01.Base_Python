class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


my_matrix = Matrix([[2, 3], [4, 5], [6, 7]])
print(my_matrix)
print()
other_matrix = [[4, 5], [7, 9], [2, 3]]

print(my_matrix + other_matrix)
