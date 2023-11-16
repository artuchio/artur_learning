# rabota s fialami otkryvaet chitaet i piwet
# 'r' - read
# 'a' - append
# 'w' - write
# 'c' - create
# 'r+'- read and write

# file = open('lor.txt', 'r', encoding='UTF8')  # 001_artur/101_practical_excersizes/lor.txt
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.closed)
#
# file.close()

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     print(file.closed)
# print(file.closed)
# with open('lor.txt', 'r', encoding='UTF8') as file:
#     file_content = file.read(20)
#     print(file_content)
#     file_content = file.read()
#     print(file_content)
#
# print(file_content)
# print(type(file_content))
# print(len(file_content))

# file_content = file.readlines()
# file_content = file.readline()
# print(file_content)
# print(type(file_content))
# print(len(file_content))
#
# for line in file_content:
#     print(line, end='')
# print()
# x = """
# ASFJKADF
# SDFJKBSDBV
# SDHAFB
# """

# with open('lor.txt', 'r', encoding='UTF8') as file:
#     read_size = 100
#     file_content = file.read(read_size)
#     while len(file_content) > 0:
#         print(file_content)
#         file_content = file.read(read_size)
#
# with open('lor.txt', 'r', encoding='UTF8') as file:

# with open('lor_copy.txt', 'w', encoding="UTF8") as file:
#     file.write("hello world\n")
#     file.write('Hello again')
#     file.write(input("Enter name: "))

# with open('lor_copy.txt', 'a', encoding="UTF8") as file:
#     file.write("hello world\n")
#     file.write('Hello again\n')
#     file.write(input("Enter name: "))

# with open('lor_copy.txt', 'x', encoding="UTF8") as file:
#     file.write("hello world\n")
#     file.write('Hello again\n')
#     file.write(input("Enter name: "))

# with open('lor_copy.txt', 'r+', encoding="UTF8") as file:
#     data = file.read().upper()
#     file.seek(0)
#     file.write(data)

with open('logo.png', 'rb') as picture:
    data = picture.read()
print(data)

with open('logo_copy.jpg', 'wb') as picture_copy:
    picture_copy.write(data)
print(data)