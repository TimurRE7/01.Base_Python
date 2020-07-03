class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income_wage = income['wage']
        self.income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self.income_wage + self.income_bonus)


pos_1 = Position('Petr', 'Petrov', 'middle', {'wage': 100000, 'bonus': 30000})
pos_2 = Position('Nikolay', 'Sidorov', 'tim-lead', {'wage': 200000, 'bonus': 50000})

pos_1.get_full_name()
pos_1.get_total_income()
pos_2.get_full_name()
pos_2.get_total_income()
