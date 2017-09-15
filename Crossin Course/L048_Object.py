#-*- coding: utf-8 -*
# Dorian Wang 2017.09.01
# lesson 48: Object example: MyClass

class MyClass:
    name = 'Sam'

    def sayHi(self):
        print('Hello %s' % self.name)

mc = MyClass()

print(mc.name)

mc.name = 'Lily'
mc.sayHi()

