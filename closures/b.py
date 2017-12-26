def catchy(phrase):
    options = [phrase.title(), DEFAULT_TITLE]
    options.sort(key=catchiness)
    return options[1]

print("Global Vars: ", catchy.__code__.co_names)
print("Local Vars: ", catchy.__code__.co_varnames)
print("Free Vars: ", catchy.__code__.co_freevars)
