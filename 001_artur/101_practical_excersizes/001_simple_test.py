'''
Написать программу которая:
	1. Высчитывает возраст из заданых данных (current_year - нынешний год, year_of_birth - год рождения)
	2. Найти недостающую часть кода (code_2)
		a. найдите остаток от x деленого на y
		b. полученый результ умножте на 13
		c. извлеките квадратный корень из полученного результата
		d. возьмите целую часть от результа
	3. Соединить код в отдельную переменную
	    пример:
	        475-12-967
	4. Вывести строку:
		пример:
			Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.
'''

# # Part1: years
current_year = int(input("What is the current Year? "))
year_of_birth = int(input("What Year You Were Born? "))
print("You are: " + str(current_year - year_of_birth) + str(" years old"))

# code parts
code_1 = '354'
code_2 =
code_3 = 132
x = 152
y = 132
#Finding (code_2)
#Step1
print(x % y)
#Step2
print(x % y)( * 13))
#Step3
print(x % y) * 13 ** 0.5

# name
user_name = 'John'
user_surname = 'Smith'



print(x % y)
#4
user_name = str(input("What is Your Name?"))
user_surname = str(input("What is Your Surname?"))
print("Dear " + user_name +
      " " + user_surname +
      "!" + " You are " +
      str(current_year - year_of_birth) +
      str(" years old.") +
      (" Your secret code is"))
