import itertools
import time

class TrafficLight:
    color = [['Красный', 7], ['Желтый', 2], ['Зеленый', 5]]

    def running(self):
        for elem in itertools.cycle(self.color):
            print(f'{elem[0]}')
            time.sleep(elem[1])

light = TrafficLight()
light.running()
