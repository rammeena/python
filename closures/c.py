HIGH_SCORE= 1000

def new_high_score(score):
    global HIGH_SCORE
    print('congrats on the high score!')
    print('old high score:', HIGH_SCORE)
    HIGH_SCORE = score

print("Global Vars: ", new_high_score.__code__.co_names)
print("Local Vars: ", new_high_score.__code__.co_varnames)
print("Free Vars: ", new_high_score.__code__.co_freevars)
