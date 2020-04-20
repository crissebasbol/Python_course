s = set([1, 2, 3])
t = set([3, 4, 5])

union = s.union(t)
print(union)

intersection = s.intersection(t)
print(intersection)

differenceS = s.difference(t)
print(differenceS)

differenceT = t.difference(s)
print(differenceT)

print(1 in s)
print(1 in t)
