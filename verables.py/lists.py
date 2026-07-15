'''fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[1])
print(fruits[3])
print(fruits[0])
fruits.append("kafal")
print(fruits)
fruits.insert(3,"sitafal")
print(fruits)'''


'''list =['Milk', 'Bread', 'Eggs', 'Butter']
list.insert(2,"jam")
print(list)
print("total items ", len(list))
x = list.pop(3)
print(x)
print(list)'''


'''cities = ["Delhi", "Mumbai", "Jaipur"]

for city in cities:
    print(city)
'''
'''
total = 100

numbers = [10, 20, 30]

for n in numbers:
    total = total + n
    print(total)'''

marks = [78,85,92,65,80]
total = 0
for mark in marks:
    total =total + mark
print("total sum ",total)

average=total/len(marks)
print("average valve is ",average)
for mark in marks :
    if mark > 80:
      print(mark)