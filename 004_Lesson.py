# #Lesson4 Upravljajushie konstrukcii
# x = 0
# if x > 0:
#     print('X is greater than zero')
# elif x < 0:
#     print('X is smaller than zero')
# else:
#     print('x is equal to zero')

# id_code = 38711111111
# if len(id_code) == 11:
#     print("ok")
# elif len(id_code) > 11:
#     print('too long')
# else:
#     print('too short') #konvertiruem integer v stroku

# id_code = 38711111111
# if len(id_code) == 11:
#     print("ok")
# else:
#     if len(id_code) > 11:
#     print('too long')
#     else:
#          print('too short')

# name = 'Samantha'
# if len(name) > 5 and len(name) < 10: #i pervoe i votore dolznhy byt true oba
#     print(name)

# if len(name) > 5 or len(name) < 10:  #tolko odno uslovie
#     print(name)

# if len(name) > 5 and len(name) < 10: #not reverse
#     print(name)
# if 'x' not in 'hello world':
#     print('ok')

#list on zhe spisok
# empty = []
# print(type(empty))
# print(bool(empty))

# empty = list()
# print(type(empty))
# print(bool(empty))

# world = 'world'
# filled_list = [1234, 123.4, 'helloworld', world, [1,[4, 5, 6], 3]]
# print(len(filled_list))
# print(filled_list[-1][1][2])

# courses = ['History', 'Programming', 'Literature', 'Physics']
# numbers = [1, 5 , 6, 8, 3, 4, 2]

# test = [1, 2, 3,]
# test[1] = 7777
# print(test)
##metod dobavlenia
# courses.append('English') # dobavljaet znachenie()tolko 1 elemnt v konec spiska
# print(courses)
# courses.isert(1, 'Art')
# courses.extend(["english", 'art'])
##metod udalenia
# courses.remove('Math')
# removed = courses.pop(1)
# print(removed)
# print(courses)courses
# courses.reverse()
# courses.sort()
# courses.sort(reverse=True)
# print(courses)
#
# numbers.sort()
# print(numbers)

# print(min(courses))
# print(max(courses))
# print(sum(numbers))

#spiski mozhno skladyvat
# print(courses + numbers)
# print(courses[:3] + numbers + courses[3:])

# print(course.index('Math', 3))
# print("Math" in courses)
# print('hello world'.split('l'))
# courses_str = ' '.join(courses) #beret spisok i sozdajot stroku
# print(courses_str)
#
# a = 10
# b = a
# a += 20
# print(a, b)\
courses = {'History', 'Programming', 'Literature', 'Physics'}
numbers = {1, 5 , 6, 8, 3, 4, 2}
# empty = tuple()
# print(type(empty))
# empty = (1,)
# print(type(empty))

# empty = set()
# print(type(empty))

# set1 = {'Math', 'History', 'Programming', 'Physics'}
# set2 = {'Art','Physics', 'Design', 'History'}
# set3 = {'Art', 'Design'}
#
# print(set1.intersection(set2))
# print(set2.difference(set1))
#
# print(set3.issubset(set2))
# print(set2.issuperset(set1))
for number in range(10)