# -*- coding: utf-8 -*
# Dorian Wang 2017.09.01
# lesson 49: Object example: Car Speed

class Car:
    speed = 0

    def drive(self,distance):
        time = distance / self.speed
        print(time)


car = Car()
car.speed = 60.0
car.drive(100.0)
