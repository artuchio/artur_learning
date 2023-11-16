# def no_parameter():
# #     print('hello world!') .... no_parameter() #chtoby vyzvat funkcii nuzno postavit ()
#     return 'Hello world!'
# # print(no_parameter())
# #x = no_paramter().upper()
#
# # def with_params(a, b):
# #     print(a ** 2)
# # with_params(11)
# # with_params(12)
# # with_params(13)
# # b = 14
# # with_params(b)
# # x = [50, 60, 70]
# # with_params(x[0])

# def odd_or_even(number):
#     if number % 2 == 0:
#         return 'EVEN'
#     else:
#         return 'ODD'
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in x:
#     print(f'{num} is  {odd_or_even(num)} number')

# def say_hello(first_name, last_name, age, gender):
#     if gender == "male":
#         return f'This is {first_name} {last_name}. He is {age} years old'
#     elif gender == "female":
#         return f'This is {first_name} {last_name}. She is {age} years old'
#
# first = input("ENTER YOUR NAME: ")
# last = input("ENTER LASTNAME: ")
# print(say_hello(first, last, 20, "female"))

# def sum_three_or_two(num1, num2, num3=0, *args, **kwargs):
#     return num1 + num2 + num3
# x = sum_three_or_two(3,4)
# print(x)
# "hello".replace()

# x = [1, 2, 3]
# y = [5, 6, 7, *x]
# print(y)

# def tester(num1, num2, num3):
#     print(num1, num2, num3)
# tester(num3=1, num2=2, num1=3)

# a = 1
# b = 2
# c = 3
# def tester():
#     global a, b, c
#     a = 10
#     b = 20
#     c = 30
#     print(a, b, c)
#
# tester()
# print(a, b, c)

# import helpers
#
# print(helpers.sqrt(144))
# print(helpers.format_name("artur", 'ZAITSEV'))

# from helpers import rectangle_area
# print(rectangle_area(10, 20))


# def hello():
#     print('HELLO')
#
# def wrapper():
#     hello()
#     hello()
#
# wrapper()


order = [
    {'size': 'small', 'qty':35'}
]