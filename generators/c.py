mylist = [[1,2],[3,4]]

def myfunc(lst):
    for node in lst:
        for subnode in node:
            yield subnode

