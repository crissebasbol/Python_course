#!/usr/bin/python
# -*- coding: utf -8 -*-


def my_first_function():
    return "Hello world"


print(my_first_function())

myList = [22, True, "una lista", 'A', [1, 2]]
print(myList)

myTuple = (22, True, "una tupla", 'B', (1, 2))
print(myTuple)

myDictionary = {"Name": "Cristhian", "Last_name": "Bolaños"}
print(myDictionary["Name"])

print(4.3)
print(int(4.3))
print(int(4.9))

print(float(4))

print(str(4.3))

print(list(myTuple))

print(len("key"))

print(type(myList))
print(type(myTuple))
print(type(myDictionary))
print(type("key"))
print(type(22))

print(map(float, [1, 2, 3, 4]))

print(round(6.2334, 1))
print(round(6.2334, 0))
print(round(6.5, 0))

print(range(5))

print(sum([1, 2, 3]))
print(sum(range(4)))

print(sorted([5, 6, 3, 1]))

print(dir(myList))


class Student(object):
    def __init__(self, name):
        self.name = name

    def presentation(self):
        return "Hi, my name es %s, nice to meet you" % self.name


student1 = Student("Cristhian")
print(student1.presentation())

a = 1
b = 2
if a > b:
    print("a>b")
elif a == b:
    print("a==b")
else:
    print("a<b")

for i in range(5):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1
