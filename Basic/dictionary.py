x = {'name': "Tom", "age": 20}
y = {"name": "Bean", "age": 25.8, True: True}
z = y.copy()
print(x, y, z)
print(x["age"], y["name"])

x['varsity'] = "MIT"  # add new item
print(x)
x.pop("varsity")  # delete an item
print(x)
