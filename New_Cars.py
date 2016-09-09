class Car(object):
    def __init__(self, engine, wheels, doors):
        self.engine = engine = None
        self.wheels = wheels = 4
        self.doors = doors = 2

    def drive(self):
        print ('Driving far...')

    def stop(self):
        print ('Pushing the brakes')

class Van(Car):
    def __init__(self, weight, wheels):
        super(self.__class__, self).__init__()
        self.weight = weight
        self.weels = wheels

    @classmethod
    def get_heavy_van(cls, *args):
        return cls(9,9, *args)




