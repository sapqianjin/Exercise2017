# -*- coding: utf-8 -*
# Dorian Wang 2017.09.01
# lesson 50: Object example: Vehicle

class Vehicle:
    def __init__(self,speed):
        # 注意是init，而不是int
        self.speed = speed

    def drive(self,distance):
        print("need %f hour(s)" % (distance / self.speed))
        # 此处如果不加self，直接用speed，就变成了调用一个在drive中的局部变量


class Bike(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle.__init__(self,speed)
        self.fuel = fuel

    def drive(self,distance):
        Vehicle.drive(self,distance)
        print("need %f fuels" % (distance * self.fuel))


b = Bike(15.0)
c = Car(80.0,0.012)

b.drive(100.0)
c.drive(100.0)
