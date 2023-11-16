# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz
# custom_range = int(input("Type your number"))
# for answer in range(custom_range):
#     if answer % 5 == 0 and answer % 3 == 0:
#         print(f"{answer}  FizzBuzz")
#     elif answer % 5 == 0:
#         print(f"{answer}  Buzz")
#     elif answer % 3 == 0:
#         print(f"{answer}  Fizz")
#     else:
#         print(answer)
######
        # if answer % 3 == 0 and answer % 5 == 0:
        #     print(f"{answer}  FizzBuzz")
        #     if answer % 3 == 0 and answer % 5 != 0:
        #         print(f"{answer}  Buzz")
        #         if answer % 5 == 0 and answer % 5 != 0:
        #             print(f"{answer}  Fizz")

# x = 0
# if x < 10:
# elif x < 9:
#     print(10)
#     elif x < 8:
#         print(10)
#          elif x < 7:
#             print(10)
#
# username = input('Enter name: ')
# if username:
#     print('Hello ' + username)
# else:
#     print('You didn\'t enter your name!')

# print ('Stratring')
# if user_name:
#     print('Hello' + user_name )
#     print('Finishing')
# username = input('Enter name: ')
# if not username.istitle():
#     user_name = username.istitle()
#     print(username)

# for x in 'hello':
#     print(x.upper())
#
#     for y in [1,2,3,4]:
#         print(y**2)
# for num1 in range(10): # smotrit 10
#     for num2 in range(10): # 10*10
#         for num3 in range(10): #10*10*10
#             for num4 in range(10):
#                 print(num1, num2, num3, num4,)

# squares = []
# for num in range(101):
#     squares.append(num**2) #dobavljaet v konec spiska
# print(squares)
#
# squares = []   #.append #dobavljaet v konec spiska
# for num in range(101):
#     squares.append(num, num**2))
#     cubes.append((num, num**3))
# print(squares)
# print(cubes)

# squares = []
# cubes = []
# for num in range(101): #cikl
#     squares.append((num, num ** 2)) # telo cickla
#     cubes.append((num, num **3))
# print(squares)
#
# for pair in squares:
#     print(f'Square of {pair[0]} is {pair[1]}')

# people = (['Jack', 'Smith', 25], ['Mary', 'Gold', 20], ['Bob', 'Dylan', 45])
# for person in people:
#     print(f'Hello {person[0]} {person[1]}. You are {person[2]} years old.')

# people = (['Jack', 'Smith', 25], ['Mary', 'Gold', 20], ['Bob', 'Dylan', 45])
# for name, surname, age in people:
#     print(f'Hello {name} {surname}. You are {age} years old.')

# people = (['Jack', 'Smith', 25], ['Mary', 'Gold', 20], ['Bob', 'Dylan', 15])
# for name, surname, age in people:
#     result = f'Hello {name} {surname}. You are {age} years old.'
#     if age < 18:
#         result += 'You are teen'
#     else:
#         result += 'You are adult'
#     print(result)

# while True: #uslovno bezkonechnyj cickl mozhem vozvrashatsa v kakoj to moment koda
#     print('I can\'t stop!')

# x = 0
# while x < 100:
#     print(x)
#     x += 1

#shagomer simulator
# step_len = 0.8
# current_position = 0
# total_steps = 0
# distance_to_target = float(input("How many km you like to travel?")) * 1000
#
# while current_position < distance_to_target: #prinimaet uslovie kotore dolgno vozvrawat True
#     current_position += step_len
#     total_steps += 1
#
# print(total_steps)

# x = 0
# while True:
#     if x > 10:
#         break
#     print(x)
#     x += 1

# for letter in 'python':
#     if letter =='h':
#         continue
#     elif letter == 'o':
#         break
#     print(letter)
#
# user_choice = input('please')
# if user_choice == '1':
#     pass
# elif user_choice == '2':
#     pass
#38803160272
while True:
    user_input = input('please enter ID code or type "exit": ')
    if user_input.lower() == 'exit':
        break
    try:
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print('Some error is not numeric')
    except UserWarning:
        if len(user_input) > 11:
            print("too long!")
        else:
            print('too short!')
    else:
        while True:
            user_choice = input('please choose:\n'
                                '1.Gender\n'
                                '2.Date of Birth\n' #dd.mm.yyyy
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '-->')
            if user_choice == '1':
                if user_input[0] not in '09':
                    if int(user_input[0]) % 2 == 0:
                        print('You are female')
                    else:
                        print('You are male')
            elif user_choice == '2':
                pass
            elif user_choice == '3':
                pass
            elif user_choice == '4':
                pass
            elif user_choice == '5':
                break #stavim potomu chto menu pomenjat
            elif user_choice == '0':
                quit() #neimeet parmetrov i argumentov
            else:
                print('Choice is out range!')

        # print(user_input)
        # break
    # finally:
    #     print('FINALLY')
