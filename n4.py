class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'Машина: {self.name}, скорость {self.speed}, цвет {self.color}')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула ' + direction)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости автомобиля {self.name}')
        else:
            print(f'Cкорость автомобиля {self.name} составляет {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости автомобиля {self.name}')
        else:
            print(f'Cкорость автомобиля {self.name} составляет {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

ford = TownCar('Ford', 70, 'black')
ford.show_speed()
audi = PoliceCar('Audi', 100, 'white')
audi.go()
audi.show_speed()
