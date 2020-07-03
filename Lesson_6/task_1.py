from time import sleep
from itertools import cycle


class TrafficLight:

    def running():
        time_sleep = [7, 2, 11]
        color = ['Красный', 'Желтый', 'Зеленый']
        for i, col in cycle(enumerate(color)):
            print(col)
            sleep(time_sleep[i])


traffic = TrafficLight
traffic.running()
