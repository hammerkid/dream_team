class Car(object):
    numbers_of_call = 0
    def __init__(self):
        pass

    @staticmethod
    def drive():
        Car.numbers_of_call += 1
        print ('Driving')


Car.drive()
Car.drive()
Car.drive()
Car.drive()
print (Car.numbers_of_call)


#------------------------------------


def __str__(self):  # when print - print what returnde
    return self.color

#-------------------------------------