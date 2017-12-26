#a.py
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
                 'julian sequeira', 'sandra bullock', 'keanu reeves',
                          'julbob pybites', 'bob belderbos', 'julian sequeira',
                                   'al pacino', 'brad pitt', 'matt damon',
                                   'brad pitt']

def clean_names(names):
    'dedup and title case names'
    return [item.title() for item in set(names)]

def sort_by_surname_desc(names):
        names = clean_names(names)
        names.sort(key=lambda name: name.split()[-1].lower(), reverse=True)
        return names

def shortest_name(names):
    names = clean_names(names)
    #names.sort(key=lambda name: name)
    #return names[0].split()[0]
    new_names = [name.split()[0] for name in names]
    return min(new_names, key=len)


x = clean_names(NAMES)
print('x: ', x)
print()
y = sort_by_surname_desc(NAMES)
print('y: ', y)
print()
print()
z = shortest_name(NAMES)
print('z: ', z)
