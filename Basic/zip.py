# zip
name = ["Tom", "Hanks", "Cruise"]
age = [21, 67, 57]

person_info = list(zip('123', name, age))
print(person_info)

# unzip
all_info = [('1', 'Tom', 21), ('2', 'Hanks', 67), ('3', 'Cruise', 57)]

unzip_all_info = list(zip(*all_info))
print(unzip_all_info)

serial = unzip_all_info[0]
print(serial)

person_name = unzip_all_info[1]
print(person_name)

person_age = unzip_all_info[2]
print(person_age)
