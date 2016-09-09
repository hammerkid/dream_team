def whiser(x):
    def wrapper_function(x):
        print('Before saying ')
        x()
        print ('After saying')
    return str(x).lower

def say_something(x):
    print(str(x))


