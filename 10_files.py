import sys

with open('work.txt', 'w') as f:
    print("Safikul", file=f)

# print("Enter your name: ", end="")
# name = ''

# sys.stdout.flush()
# while True:
#     c = sys.stdin.read(1)
#     if c == '\n':
#         break
#     else:
#         name = name+c

# print(f"Yoour name is {name}")


# print(sys.argv[0])
# print("-----------------------------")
# with open('work.txt', 'r') as file:
#     contents = file.read()
#     print(contents)
#     print("-----------------------------")
#     file.seek(0, 0)
#     print(file.read(5))
#     print(f"current cursor position in {file.tell()}")
#     print(file.read(9))

# with open('work.txt', 'r') as file1:
#     line = file1.readline()
#     print(line)
#     print(line.rstrip())
#     print(line.rsplit())

# with open('work.txt', 'r') as file2:
#     while True:
#         line = file2.readline()
#         if not line:
#             break
#         else:
#             print("-----------------------------")
#             print(line)
#             print(line.rstrip())
#             print(line.rsplit())

# with open('work.txt', 'r') as file3:
#     for line in file3:
#         print(line.rstrip())

# with open('work.txt', 'r') as file4:
#     contents=file4.readlines()
#     for i in contents:
#         print(i.rstrip())

# text = '''Incompatible, it don't matter though
# 'cos someone's bound to hear my cry
# Speak out if you do
# You're not easy to find\n'''

# with open('work.txt', 'a') as file4:
#     file4.write(text)  # Replacing all the contents

# with open('work.txt', 'r') as file5:
#     content = file5.read()
#     print(content)  # Appending at the end of the previous content
