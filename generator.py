a='ABC'
def generator (string):
    for letter in a:
        yield letter


g = generator(a)

while True:
    try:
        print (next(g))
    except StopIteration:
        print ('stop iter')
        break
