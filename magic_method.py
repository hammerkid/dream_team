class Car():
    def __init__(self, name, color='white'):
        self.color = color
        self.name = name
        print ('Car {} created'.format(self.name))

    def __del__(self):
        print ('Car {} yok'.format(self.name))

    def __repr__(self):
        return 'Car {} here'.format(self.name)

mazda = Car('mazda')
zaz = Car('zaz')
print zaz
