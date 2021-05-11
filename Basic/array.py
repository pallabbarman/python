from array import *

salary = array('i', [15987, 75321, 654789, 12345])
for i in range(4):
    print(salary[i])

salary.append(40000)
salary.remove(15987)
salary.reverse()

salary1 = array('f', [15987.45, 75321, 654789.48, 12345])
for i in range(4):
    print(salary1[i])
