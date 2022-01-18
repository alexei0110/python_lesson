class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

station = Stationery("Рисунок")
station.draw()
my_pen = Pen("Ручка")
my_pencil = Pencil("Карандаш")
my_handle = Handle("Маркер")
my_pen.draw()
my_pencil.draw()
my_handle.draw()
