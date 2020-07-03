class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self, direction):
        print('{} is turning {}'.format(self.name, direction))

    def show_speed(self):
        print('current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('current speed:', self.speed)
        if self.speed > 40:
            print('Your speed is more than max!')


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'Yellow', 'Town car', False)
sport_car = SportCar(180, 'Blue', 'Sport car', False)
work_car = WorkCar(30, 'Green', 'Work car', False)
police_car = PoliceCar(150, 'Black', 'Sport car', True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
work_car.turn('right')
