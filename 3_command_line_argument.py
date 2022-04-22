#!/usr/bin/env python
# 3_command_line_argument.py

# run this file as
# python 3_command_line_argument.py 1 2 3 4 5 6   <---- Arguments

import sys

print("Script name", sys.argv[0])
print("Arguments: ")
for arg in sys.argv[1:]:
    print(arg)
