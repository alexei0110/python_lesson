class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self.income.values())

worker = Position("John", "Legend", "singer", 100000, 50000)
print(worker.get_full_name())
print(worker.position)
print(worker.get_total_income())
