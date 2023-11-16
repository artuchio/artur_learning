# # Part1: years
current_year = int(input("What is the current Year? "))
year_of_birth = int(input("What Year You Were Born? "))
# print("You are: " + str(current_year - year_of_birth) + str(" years old"))

# Part2: Code_2
code_1 = '354'
code_2 = 16
code_3 = 132
x = 152
y = 132
#Step1
# print(x % y)
# # #Step2
# print((x % y) * 13)
# # #Step3
# print(((x % y) * 13) ** 0.5)
# # Step4
# print(int(((x % y) * 13) ** 0.5))

#Part3
#Step1 convert integer to string
secret_code = code_1 + "-" + str(code_2) + "-" + str(code_3)
# print(secret_code)
#4
user_name = str(input("What is Your Name?"))
user_surname = str(input("What is Your Surname?"))
print("Dear " + user_name +
      " " + user_surname +
      "!" + " You are " +
      str(current_year - year_of_birth) +
      str(" years old.") +
      (" Your secret code is ") + str(secret_code))
############################################### Answer
# /usr/local/bin/python3.9 /Users/abhishekmathur/PycharmProjects/artur_learning/001_artur/001_simple_data_types_and_operators/Hommie.py
# What is the current Year? 2023
# What Year You Were Born? 1987
# What is Your Name? Artur
# What is Your Surname? Zaitsev
# Dear  Artur  Zaitsev! You are 36 years old. Your secret code is 354-16-132
# Process finished with exit code 0