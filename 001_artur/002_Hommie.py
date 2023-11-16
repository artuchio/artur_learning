# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1[:2] + example_string1 [-2:])

# # Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())
# # Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip("*"))
print(example_string3.rstrip("*")) #tolko sleva # .lstrip
#
# # Write a code to return "Hello my name is Jack"
example_string4 = "hello my naMe is jack"
print(example_string4.capitalize())
print(example_string4.capitalize().replace ('jack', "Jake"))


#
#
# # Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
output_1 = var2.title() +(', ')+ var3.swapcase() +(" ") + var1.title()
print(output_1)
print(f'{var2.title()} + (', ')+ {var3.swapcase()} +(" ") + {var1.title()}

# # Write a code to return byte_string text value
# # 'utf-8' 'utf-16' cp1257 cp 1252
byte_string = b"\316\273"
print(byte_string.decode('utf-8'))

#########
print(full_name.title())
#########
import string
sample = 'Hello, my name is Jack! I am from London -United Kingdom. Where are you from?'
symbols = str.maketrans('','', string.punctuation) #python tutorials & programiz
print(string_punctuation)
print(type(string_punctuation))
print(sample.replace(',', ' ') .replace('.', ' ').replace('!', ' '))
##########
user_input = input("enter smtgh")
print(len(user_input.replace(' ', '')))
print('...\\')