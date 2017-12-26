from collections import Counter

responses = [
        "vanilla",
        "chocolate",
        "vanilla",
        "vanilla",
        "caramel",
        "strawberry",
        "strawberry",
        "vanilla"
        ]

print((Counter(responses)))
print(type(Counter(responses).most_common()))
print(type(Counter(responses).most_common(1)))
print(type(Counter(responses).most_common(1)[0]))
print(type(Counter(responses).most_common(1)[0][0]))

print("The children voted for {} icecream".format(Counter(responses).most_common(1)[0][0]))

