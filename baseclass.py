class Car(object):
    def __init__(self, doors, color, wheels = 4):
        self.doors = doors
        self.color = color
        self.wheels = wheels
        self.tank = 90

    def ride(self):
        self.doors = 'closed'
        self.tank = self.tank - 1
        print (self.doors + ' ' + 'moving')

    @property
    def fill_tank(self):
        if self.tank < 90 :
            print ('Small tank, replace')
        return self.tank

    @fill_tank.setter
    def fill_tank(self, new_value):
        if new_value > 90:
            print ('replaced bigger tank')
            self.tank = new_value

mazda = Car(4,'white')
print (mazda.tank)
mazda.fill_tank = 100
print (mazda.tank)