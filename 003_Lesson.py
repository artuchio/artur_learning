# string_sample1 = "Hello world world"
# string_sample2 = "first leTter is loWercase. new-sentence"
# string_sample3 = "*   **extra symbols   "
# german_sample = "der fluß"
#
# # print(len(string_sample1))
# # print(type(len(string_sample1)))
# #
# # print(string_sample1[0]) #otchet nachinaetsa ot 0,1,2,3 (#indexirovanie stroki)
# # print(string_sample1[len(string_sample1) - 1])
# # print(string_sample1[0])
# # print(string_sample1[-15])
# # print(string_sample1[0:5]) # v pythone poslednii simvol ne vkljucheno ot pervogo ne vkljuchaja poslednee [START:END]
# # print(string_sample1[6:11])
# # print(string_sample1[:5]) #snahala do konca
# # print(string_sample1[5:]) #s simvola do konca
# # print(string_sample1[0:14:3])
# # print(string_sample1[::-1]) #samyj prostoj sposob razvernut stroku (polindrom)
# # print("hello world)" [::-1])
# # #perobjavit znachenie
# # #[START:END:STEP]
# # print(string_sample1[:5] + string_sample2 [0:])
#
# print("world" in string_sample1) #vsegda vozvrashaet bool
# print("a" == "A") #logika cifry potom zaglavnye propiusnye
# print("world < World")
# #methody konvertacii registra bukv
# print(string_sample2.upper())
# print("Hello".isupper())
# print(german_sample.lower())
# print(german_sample.casefold())
#
# print("HELLO world".swapcase()) #menjaet sbolshih na malenkie
# print(string_sample2.capitalize())
# print(string_sample2.title())
# print(string_sample2.istitle()) #vse li slowa nachinajutsa s bolshoi bukvy
#
# print(string_sample3.strip()) #method s dop argumentami (vyrezaet probely)
# print(string_sample3.strip("*"))
# print(string_sample3.strip("* ")) #sleva i sprava v nachale i konce stroki
# print(string_sample1.replace("w", "W"))
# print(string_sample1.replace("world world", ""))
# print(string_sample1.replace("world ", "", 1))
#
# print("hello poeople, of planet earth".split()) #probely
# print("hello poeople, of planet earth".split(", "))
# print(string_sample1.count("world"))
# print(string_sample1.count("world", 7)) #poshictaj s opredeljonnogo simvola
# print(string_sample1.find("world")) #pokazyvaet index i ishet pervoe popavsheesja no tolko odno
# #w3skoools.com/ tutorial python /refernece /string reference
#
# print('hello', 'planet', '123', sep="", end='!!')
# print('hello', 'planet', '123', sep="", end='\n') #\n simvol perenosa izbegaet standartnoe povedenioe simvolov
# print('World')
# print(r'\tHello\ne\'w')
# # \
# # \\
# # \n
# # \t #tabuljacia (4 probela)
# # \b
# # \f
# # \ooo
# # \xhh
# name = 'John'
# salary = 1000
# age = 36
# salary_str = '{} salary is {}. age:{}'
# print(salary_str.format(name, salary, age))
# salary_str = '{2} salary is {1}. age:{0}{0}'
# print(salary_str.format(name, salary, age)
# salary_str = {user_name}s salary is {user_salary}. Age: {user_age}
# print(salary_str.format(user_name=name, user_age, user_salary))
# name = 'John'
# salary = 1000
# age = 36
# print(f'{name}s salary is {salary:.2f}. He is {age} years old.')
# print(f'{name.upper()}s salary is {int(salary)}. He is {age} years old.')
#.encode .decode