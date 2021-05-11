list1 = [1, 10, 5.7, 9, 22, 47, 'Tom']
print(list1)

list2 = [1, 45, 5, 8.3, [45, 2.1, 98, 45]]
print(list2)
print(list2[1])

list3 = list1+list2
print(list3)

list3.remove(list3[3])
print(list3)

list4 = list3.count(1)
print(list4)
