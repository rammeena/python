#merge_dicts.py

route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

print("Individual dictionaries: ")
print("route: {}".format(route))
print("query: {}".format(query))
print("post:  {}".format(post))

#1. Non-pythonic procedural way (item by item)
m1 = {}

for k in route:
    m1[k] = route[k]
for k in query:
    m1[k] = query[k]
for k in post:
    m1[k] = post[k]

#2. Non-pythonic procedural way (item by item)
m2 = {}
for d in [route, post, query]:
    for k, v in d.items():
        m2[k] = v

#3. dict methods way
m3 = route.copy()
m3.update(query)
m3.update(post)


#4. dict comprehension methods way

m4 = {k:v for d in [route, query, post] for k,v in d.items()}

#5. advance dict comprehension methods way

m5 = {**route, **query, **post}
