#a.py
def tally():
    score = 0
    print("Inside func")
    while True:
        print("Inside while")
        increment = yield score
        score += increment
