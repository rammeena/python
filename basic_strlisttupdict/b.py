#b.py
mylist = ['b', 'b', 'a', 'a', 1, 2, 3, 4, 1, 2, 3, 5, 6, 7]

new_list = []

for n,i in enumerate(mylist):
    if i not in mylist[:n]:
        new_list.append(i)

print(new_list)

