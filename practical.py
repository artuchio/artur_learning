# Практикум 1:
#
# 1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#     Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>
#
# 2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (
# с = sqrt(a * a  +  b * b))
#
# 3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет, является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5
#
# 4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке.
#
# 5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить кортеж B таким образом, что кортеж B помещается на index[2].
#     Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)
#
# 6 *Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#     Примеры:
#     [1, 2, 3, 4, 7, 9, 9] → [9]
#     [1, 2, 4, 6, 4, 6] → [4,6]
#
# 7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#     Примеры:
#     1234565 seconds = 14:6:56:5
# first_name, last_name, age = input('enter n, surname and age. Use ',' as separator: ').split #variant vvoda postrochno
# user_name = str(input("What is Your Name?"))
# user_surname = str(input("What is Your Surname?"))
# user_age = input ('How old are you?')
# print("Dear " + user_name +
#       " " + user_surname +
#       "!" + " You are " +
#      user_age + "years old")

# a = float(input("enter side A: "))
# b = float(input("enter side B: "))
# c = (a * b + b * b) ** 0.5
# print(str(c))
#include??? #povotrit 3 kita ciklov
# a = float(input("enter side A: "))
# b = float(input("enter side B: "))
# c = float(input("enter side C: "))
# с**2 == (a**2) + (b**2)
#
# print(bool(p_t))

# user_list = ["apple", "banana", "cherry"]
# user_list.reverse()
# for item in user_list:
# print(item)

# t_1 = (1, 2, 3, 5, 8)
# t_2 = (8, 2, 5)
#
# index = 2
# t_1_1 = t_1[:index]
# t_1_2 = t_1[index:]
# result = t_1_1 + t_2 + t_1_2
#result = tuple(t_1)
# print(result)
#############################
# a = (1, 2, 3, 5, 8)
# b = (8, 2, 5)
# print(id(a)) #funkcia vypolnjaet proverki unikalnogo id  shohranenngo v pamjati piton
# test_list = [1,2,3,4,4,5,5,5,7,8,8,8,10,10]
# result = []
# max_count = 0
# for num in test_list:
#     if test_list.count(num) > max_count:
#         max_count = test_list.count(num)
# for num in test_list:
#     if test_list.count(num) == max_count:
#         result.append(num)
# print(list(set(result)))

# test_list = [1,2,3,4,4,5,5,5,7,8,8,8,10,10]
# result = []
# max_count = 0
# for num in test_list:
#     if test_list.count(num) > max_count:
#         max_count = test_list.count(num)
# for num in test_list:
#     if test_list.count(num) == max_count and num not in result:
#         result.append(num)
# print(result)

# test_list = [1,2,3,4,4,5,5,5,7,8,8,8,10,10]
# result = {}
# for num in test_list:
#     result[num] = test_list.count(num)
# res = []
# for key in result.keys():
#     if result[key] == max(result.values()):
#     res.append(key)
# print(result)

seconds = 1234565

days = seconds // (24*60*60)
seconds %= 24*60*60
hours = seconds // (60*60)
seconds %= 60*60
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{seconds}')