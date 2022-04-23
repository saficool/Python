#!usr/bin/env python
# 6_strings.py

# A tuple is an immutable sequence data type. The tuple can contain mixed data types.

names = ("Nur Hossain", "Sabia", "Safikul", "Bellal", "Sumi")
fruits = "oranges", "apples", "bananas"
print(names)
print(type(names))
print(fruits)
print(type(fruits))

first = (1, 2, 3)
second = (4, 5, 6)
print("length of first:", len(first))
print("length of second:", len(second))
print("first + srcond:", first+second)
print("first * 3:", first*3)
print("1 in first", 1 in first)
print("3 in second:", 3 in second)
print("5 not in second:", 5 not in second)

five = (1, 2, 3, 4, 5)
print("five[0] : ", five[0])
print("five[-1] : ", five[-1])
print("five[-2] : ", five[-2])
print("five[:] : ", five[:])
print("five[0:4] : ", five[0:4])
print("five[1:2] : ", five[1:2])
print("five[:2] : ", five[:2])
print("five[:-1] : ", five[:-1])
print("five[:9] : ", five[:9])

mix = (1, 2, "solaris", (1, 2, 3))
print("mix[1] :", mix[1])
print("mix[2] :", mix[2])
print("mix[3] :", mix[3])
print("mix[3][0] :", mix[3][0])
print("mix[3][1] :", mix[3][1])
print("mix[3][2] :", mix[3][2])

print((3 + 7))
print((3 + 7, ))
