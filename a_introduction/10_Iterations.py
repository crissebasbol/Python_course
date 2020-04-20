print(list(range(5)))
print(list(range(5, 40, 3)))

print("-----------------")

for i in range(3):
    print("Hello {}".format(i))

print("-----------------")

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i)

print("-----------------")

for i in range(30):
    if i == 22:
        break
    elif i % 3 == 0:
        print(i)

print("-----------------")

r = "Railway"

for letter in r:
    print(letter)

print("-----------------")

i = 0
while i <= 10:
    print(i)
    i += 1

print("-----------------")


