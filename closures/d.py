def tallest_building():
    buildings = {'Burj Khalifa': 828,
                 'Shanghai Tower': 632,
                 'Abraj Al-Bait': 601
                }
    x = {'a': 1}

    def height(name):
        return buildings[name]
        

    return max(buildings.keys(), key=height)

print("Global Vars: ", tallest_building.__code__.co_names)
print("Local Vars: ", tallest_building.__code__.co_varnames)
print("Free Vars: ", tallest_building.__code__.co_freevars)
