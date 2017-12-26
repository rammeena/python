#pt3.py
#import pt2

print('*' * 100)
module_global_var = 'I am modules global var'
print('module_global_var............defined')
print('*' * 100)
def upperfunc():
    pass

print('upperfunc............defined')
class module_class:
    pass

print('module_class............defined')
print('=' * 100)
print('printing function1 things')
print('=' * 100)
def function1(function1_arg1='function1_arg1'):
    x = 10
    y = 20
    name = 'Ram Meena'
    print("printing locals()...")
    print(locals())
    print("printing globals()...")
    print(globals())
    print("printing dir()...")
    print(dir())
    print("printing vars()...")
    print(vars())
function1()

class middle_class:
    pass

print('=' * 100)
print('printing chutiafunction things')
print('=' * 100)
def chutiafunction(chutiafunction_arg1='chutiafunction_arg1'):
    chuvar1 = 100000
    chuvar2 = 200000
    chuname = 'python fuck'
    print("printing locals()...")
    print(locals())
    print("printing globals()...")
    print(globals())
    print("printing dir()...")
    print(dir())
    print("printing vars()...")
    print(vars())
chutiafunction()

print('=' * 100)
print('printing global things')
print('=' * 100)
print("name of this module is %s"% __name__)
print()
print("printing locals()...")
print(locals())
print("printing globals()...")
print(globals())
print("printing dir()...")
print(dir())
print("printing vars()...")
print(vars())
