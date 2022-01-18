class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asf_mass(self):
        weigth = 25
        tickness = 5
        mass = self.length * self.width * weigth * tickness / 1000
        print(f'Необходимо {mass} тонн для строительства')

road = Road(5000, 20)
road.asf_mass()
