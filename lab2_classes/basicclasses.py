#!/usr/bin/env python3

# Basic classes to create a modular vehicle
# Theoretically can be extended to create specific vehicle classes like:
# Car, Truck, Train, Aircraft

# Classes:
# MovementSystem -> Wheels
#                -> Tracks
# Propulsion -> CombustionEngine
#            -> TurbineEngine
# Vehicle <- Propulsion + MovementSystem

class MovementSystem:
    def __init__(self, base_speed):
        self.base_speed = base_speed

    def get_fullspeed(self):
        return self.base_speed

    def __repr__(self):
        return f'<{self.__class__.__name__}: base_speed = {self.base_speed}>'

class Wheels(MovementSystem):
    def __init__(self, base_speed, count):
        super().__init__(base_speed)
        self.count = count

    def get_fullspeed(self):
        return (self.base_speed * self.count)

    def __repr__(self):
        return f'<{self.__class__.__name__}: base_speed = {self.base_speed}, amount = {self.count}>'

class Tracks(MovementSystem):
    def __init__(self, base_speed, width):
        super().__init__(base_speed)
        self.width = width

    def get_fullspeed(self):
        return (self.base_speed * (1 + 1 / self.width))

    def __repr__(self):
        return f'<{self.__class__.__name__}: base_speed = {self.base_speed}, width = {self.width} cm>'

class Propulsion:
    def __init__(self, power, fuel_amount):
        self.power = power
        self.fuel_amount = fuel_amount
        self.is_on = False

    def get_fullpower(self):
        return self.power

    def toggle(self):
        self.is_on ^= True

    def get_state_str(self):
        return 'on' if self.is_on else 'off'

    def __repr__(self):
        return f'<{self.__class__.__name__}: power = {self.power} hp, fuel = {self.fuel_amount}L, state = {self.get_state_str()}>'

class CombustionEngine(Propulsion):
    def __init__(self, power, fuel_amount, pistons):
        super().__init__(power, fuel_amount)
        self.pistons = pistons
        self.calc_consumption()

    def calc_consumption(self):
        self.consumption = (self.fuel_amount * self.pistons) / (self.power * 0.2)

    def get_fullpower(self):
        return (self.power / self.pistons)

    def __repr__(self):
        return f'<{self.__class__.__name__}: power = {self.power} hp, fuel = {self.fuel_amount}L, pistons = {self.pistons}, consumption = {self.consumption:.2f} L/h, state = {self.get_state_str()}>'
        
class TurbineEngine(Propulsion):
    def __init__(self, power, fuel_amount, throttle):
        super().__init__(power, fuel_amount)
        self.throttle = throttle    # 0-100
        self.calc_consumption()

    def calc_consumption(self):
        self.consumption = (self.fuel_amount * self.throttle) / (self.power * 0.45)

    def get_fullpower(self):
        return (self.power * (self.throttle / 100)) 

    def inc_throttle(self):
        if self.throttle < 100:
            self.throttle += 10
        self.calc_consumption()

    def dec_throttle(self):
        if self.throttle >= 10:
            self.throttle -= 10
        self.calc_consumption()

    def __repr__(self):
        return f'<{self.__class__.__name__}: power = {self.power} hp, fuel = {self.fuel_amount}L, throttle = {self.throttle}%, consumption = {self.consumption:.2f} L/h, state = {self.get_state_str()}>'

class Vehicle:
    def __init__(self, name, propultion, movement):
        self.name = name
        self.propultion = propultion
        self.movement = movement
        self.calc_speed()

    def calc_speed(self):
        self.speed = self.movement.get_fullspeed() * self.propultion.get_fullpower()

    def __repr__(self):
        return f'<{self.__class__.__name__}: name = {self.name}, speed = {self.speed:.1f} km/h\n\t{self.propultion}\n\t{self.movement}>'

def main(args):
    # car
    engine = CombustionEngine(100, 250, 4)
    movement = Wheels(0.80, 4)
    car = Vehicle('Car', engine, movement)
    car.propultion.toggle()
    print(car)
    # tank
    engine = TurbineEngine(400, 800, 60)
    movement = Tracks(0.1, 10)
    tank = Vehicle('Tank', engine, movement)
    tank.propultion.toggle()
    print(tank)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
