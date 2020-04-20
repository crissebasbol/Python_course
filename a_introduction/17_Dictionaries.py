my_dictionary1 = {
    "first_element": "1",
    "second_element": "2"
}

print(my_dictionary1)

my_dictionary2 = dict()

my_dictionary2["first_element"] = "Hello"
my_dictionary2["second_element"] = "Bye"

print(my_dictionary2)
print(my_dictionary2["first_element"])

my_dictionary3 = dict([
    ("first_element", "primer elemento"),
    ("second_element", "Segundo elemento")
])
print(my_dictionary3)

# Iteration

notes = {}

pass

notes["math"] = 4.6
notes["science"] = 5
notes["biology"] = 3
notes["apps"] = 4

print(notes)

for value in notes.values():
    print(value)

for key in notes.keys():
    print(key)

for key, value in notes.items():
    print("key: {}, value: {}".format(key, value))


# Notes average

sum_notes = 0

for value in notes.values():
    sum_notes += value

average = sum_notes / len(notes)
print("The notes average is: {}".format(average))
