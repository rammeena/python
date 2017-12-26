#comprehension.py

import collections
import uuid
Measurement = collections.namedtuple('Measurement', 'id x y value')
measurements = [
        Measurement(str(uuid.uuid4()), 1, 1, 72),
        Measurement(str(uuid.uuid4()), 2, 1, 40),
        Measurement(str(uuid.uuid4()), 3, 1, 11),
        Measurement(str(uuid.uuid4()), 2, 1, 90),
        Measurement(str(uuid.uuid4()), 2, 2, 60),
        Measurement(str(uuid.uuid4()), 2, 3, 73),
        Measurement(str(uuid.uuid4()), 3, 1, 40),
        Measurement(str(uuid.uuid4()), 3, 2, 44),
        Measurement(str(uuid.uuid4()), 3, 3, 90)
        ]

# C - Style

high_measurements1 = []  # all with value over 70
for m in measurements:
    if m.value > 70:
        high_measurements1.append(m.value)
print("C - Style :", high_measurements1)
print()
# list comprehension
high_measurements2 =[m.value for m in measurements if m.value > 70]
print("list comprehension :", high_measurements2)
print()

# generator expression
high_measurements_gen = (m.value for m in measurements if m.value > 70)

# process the generator to get something printable.
print("process the generator to get something printable")
high_measurements3 = list(high_measurements_gen)
print("generator comprehension :", high_measurements3)
print()

# dict comprehension
high_m_by_id = {m.id: m.value for m in measurements if m.value > 70}

print(" dict comprehension: ", high_m_by_id)
print()

# set comprehension
high_values_distinct = {m.value for m in measurements if m.value > 70}
print(" set comprehension: ", high_values_distinct)
print()


