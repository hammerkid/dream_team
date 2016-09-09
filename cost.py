from pprint import pprint as pp
from operator import itemgetter
eng_type_gas = 'gas'
eng_type_diesel = 'diesel'


class Car(object):
    car_pool = []
    def __init__(self, eng_type, cost, mileage):
        self.eng_type = eng_type
        self.cost = cost
        self.mileage = mileage
        Car.car_pool.append(self)

    def __eq__(self, other):
        return self.cost == other.cost

    def __repr__(self):
        return ', '.join(str(self.__dict__[_]) for _ in self.__dict__)

    def __getitem__(self, item):
        return getattr(self.item)

a = Car(eng_type_diesel, 100, 400)
b = Car(eng_type_diesel, 200, 200)
# Car(eng_type_diesel, 180, 100)
# Car(eng_type_gas, 300, 1400)
# Car(eng_type_gas, 350, 1200)
# Car(eng_type_gas, 800, 1200)
#
# pp(Car.car_pool)
# diesels = filter(lambda x: x.eng_type == eng_type_diesel, Car.car_pool)
# s_diesels = sorted(diesels, key=itemgetter('cost', 'mileage'))
# pp(diesels)

print(a == b)