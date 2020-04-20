names = ["Pedro", "Andrea", "Juan"]

print(names)
print(names[-3])

names2 = list()

names2.append("Pepito")
names2.append("Lola")

print(names2)

print(names2[0])

del names2[1]

print(names2)

myList = [1]
myList2 = [2, 3, 4]
myList3 = myList + myList2

print(myList3)

myList4 = ["a"]
myList5 = myList4 * 3

print(myList5)

myList5.append("b")

deleted = myList5.pop()

print(deleted)
print(myList5)

house = "house"
house_list = list(house)

print(house_list)
print("".join(house_list))
