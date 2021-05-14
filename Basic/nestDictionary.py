student = {1: {"name": "Tom", "age": 24, "sex": "male"},
           2: {"name": "Cruise", "age": 57, "sex": "male"},
           3: {"name": "Hanks", "age": 67, "sex": "male"}}
print(student)
print(student[1]['sex'])
print(student[3]['age'])

student[3] = {}
student[3]['name'] = "Holland"
student[3]['age'] = 20
student[3]['sex'] = 'male'
print(student)

del student[3]['sex']  # delete a single item
print(student[3])

del student[3]  # delete full item
print(student)
