# class Summation(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def sum(self):
#         self.contents = self.a+self.b
#         return self.contents


# summation = Summation(2, 3)
# print(summation.sum())


# def func(a, b):
#     """
#     This function takes two parameters and sum it then return sum value and first parameter valu
#     """
#     sum = a+b
#     return sum, a, __doc__


# _sum, _a, _doc = func(3, 5)
# print(_sum)
# print(_a)
# print(_doc)


# def plus(*args):
#     return sum(args)


# _sum = plus(1, 2, 3, 4, 5)
# print(_sum)

# _x=lambda a: a*2
# print(_x(4))

# from functools import reduce

# my_list = [1,2,3,4,5,6,7,8,9,10]

# # Use lambda function with `filter()`
# filtered_list = list(filter(lambda x: (x*2 > 10), my_list))

# # Use lambda function with `map()`
# mapped_list = list(map(lambda x: x*2, my_list))

# # Use lambda function with `reduce()`
# reduced_list = reduce(lambda x, y: x+y, my_list)

# print(filtered_list)
# print(mapped_list)
# print(reduced_list)

#!/usr/bin/env python

"""
The ret.py script shows how to work with
functions in Python.
Author: Jan Bodnar
ZetCode, 2019
"""


def show_module_name():

    print(__doc__)


def get_module_file():

    return __file__


a = show_module_name()
b = get_module_file()

print(a, b)
