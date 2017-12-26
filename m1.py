# m1.py
def myfnc():
    print('m1 module name=%s' %(__name__))

print("Printing function name using '__name__'")
print(myfnc.__name__)
print("Printing function name using '__qualname__'")
print(myfnc.__qualname__)
print("Printing function code using '__code__'")
print(myfnc.__code__)

if __name__ == '__main__':
    print('call myfnc()')
    myfnc()
