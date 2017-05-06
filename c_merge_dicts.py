from __future__ import print_function

route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

print("Individual dictionaries: ")
print("route: {}".format(route))
print("query: {}".format(query))
print("post: {}".format(post))

# Non_pythonic procedural way (item by item)
m1 = {}
for k in query:
    m1[k] = query[k]
for k in route:
    m1[k] = route[k]
for k in post:
    m1[k] = post[k]

# Classic pythonic way (copy & update)
m2 = query.copy()
m2.update(route)
m2.update(post)

# Via dictionary comprehensions {k:v in dict_list for k,v in d.items()

m3 = {k: v for d in [route, query, post] for k, v in d.items()}

# Python 3.5+ pythonic way, warning crashes on python <== 3.4

m4 = None


print(m1)
print(m2)
print(m3)
print(m4)
