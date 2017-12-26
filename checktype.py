from types import *
def checkit(x):
    if type(x) == int:
        print('You have entered an integer {}'.format(x))
    else:
        print('Unable to recognize the input data type.')

