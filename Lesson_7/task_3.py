class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        self.result = Cell(self.quantity + other.quantity)
        return self.result

    def __sub__(self, other):
        self.result = Cell(int(self.quantity - other.quantity))
        return self.result

    def __mul__(self, other):
        self.result = Cell(int(self.quantity * other.quantity))
        return self.result

    def __truediv__(self, other):
        self.result = Cell(round(self.quantity // other.quantity))
        return self.result


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells_1 = Cell(5)
cells_2 = Cell(2)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1)
print(cells_2.make_order(5))
print(cells_1.make_order(10))
print(cells_1 / cells_2)