# def squares_generator(start, end):
#     for num in range(start, end + 1):
#         yield num ** 2
# def inifinite_counter(start):
#     while True:
#         start += 1
#         yield start - 1
#
# x = squares_generator(1, 100)
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# for i in x:
#     print(i)
#
# print(next(x))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def squares(number):
#     return number ** 2
# new_nums = map(squares, numbers)
# # new_nums = []
# # for num in numbers:
# #     new_nums.append(squares(num))
# print(list(new_nums))
#

# def change_dict(d):
#     make, model, serial = d['make'], d['model'], d['serial']
#     return{
#         serial: {
#             'make': make,
#             'model': model
#         }
#     }
# cars = [
#     {
#         'make': 'VW'
#         "model": 'Golf'
#         'serial': '354678bhvft'
#     },
#     {
#         'make': 'BMW'
#         "model": '320i'
#         'serial': '3465uriftyt'
#     },
#     {
#         'make': 'Seat'
#         "model": 'leon'
#         'serial': '356hkkhu32vft'
#     }
# ]

# new_cars = map(change_dict, cars)
# print(list(new_cars))

# def power(a, b):
#     return a ** b
# nums1=[1, 2, 3, 4, 5]
# nums2=[6, 7, 8, 9, 5]
#
# new = map(power, nums1, nums2)
# print(list(new))
# # print(sum(list(new)))
# nums1=[1, 2, 3, 4, 5]
# nums2=[6, 7, 8, 9, 5]
# def odd_or_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# new = filter(odd_or_even, nums1) #otbor cherez funkciju(sozdajot novyj spisok) True idut, False ne idut
# print(list(new))

# data1=[1, 2, 3, 4, 5]
# data2=['mon', 'tue', 'wed', 'thu', 'fri']
#
# new = zip(data1, data2)
# print(list(new))
#######################
import itertools

# counter = itertools.count()
#
# print(list(zip([10, 20, 30, 40], counter)))
#
# data = [100, 200, 300, 400, 500]
# data2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(list(itertools.zip_longest(dat, data2, counter)))
# counter = itertools.count(start=10, step=5)
# counter = itertools.cycle([1, 2, 3])
# counter = itertools.repeat(3, times=4)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#sozdaem 4 vida kombinacii
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]
names = ['Jack', 'Mary']
# #NO ORDER NO REPEAT
# result = itertools.combinations(letters, 4)
#ORDER NO REPEAT
# result = itertools.permutations(letters, 2)
#ORDER REPEAT
# result = itertools.product(letters, numbers, repeat=4) #Max combination
#NO ORDER repeat
# result = itertools.combinations_with_replacement(letters, 4)
# for c in result:
#     print(c)
# import random (bibilioteka sluchainyh chisel) dljq kubikov

# result = itertools.compress(letters, numbers)
# print(list(result))
# result = itertools.filterfalse(lambda x: x > 2, numbers2)
# print(list(result))

# result = itertools.dropwhile(lambda x: x > 2, numbers2) #do pervogo fals vse do konca spiska skidyvaetsa v spisok
# result = itertools.takewhile(lambda x: x >2, numers2 ) #do pervogo true vse do konca
# print(list(result))

# result = itertools.accumulate(numbers2) #kazhdoe posleduyuwee skladyvaetsa
# print(list(result))

people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
{
        'name': 'Lee Hong',
        'city': 'Tallinn'
    }
]
people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, lambda x: x['city'])

for key, group in result:
    # print(key, group)
    print(list(group))