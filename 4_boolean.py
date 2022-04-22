#!usr/bin/env python
# 4_boolean.py


from cmath import nan
import random

male = False
male = bool(random.randint(0, 1))

if male:
    print("He's name will be Safikul")
else:
    print("her name will be Lisa")

# ----------------------------------------------
print(bool(True))
print(bool(False))
print(bool("text"))
print(bool(""))
print(bool(''))
print(bool(' '))
print(bool(1))
print(bool(0))
print(bool(3))
print(bool(nan))
print(bool(None))
