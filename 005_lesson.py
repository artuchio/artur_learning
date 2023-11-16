# 38803160272
while True: #
    user_input = input('Please enter ID code or type "exit": ')
    if user_input.lower() == 'exit':
        break
    try:
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print('ID code is not numeric!')
    except UserWarning:
        if len(user_input) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
    else:
        while True: #menu while cycle
            user_choice = input('Please choose:\n'
                                '1.Gender\n'
                                '2.Date of birth\n'  # dd.mm.yyyy
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '--> ')
            if user_choice == '1':
                if user_input[0] not in '09':
                    if int(user_input[0]) % 2 == 0:
                        print('You are female!')
                    else:
                        print('You are male!')

            elif user_choice == '2':
                if user_input[0] not in '09':
                    if user_input[0] in '12':
                        year = '18'
                    elif user_input[0] in '34':
                        year = '19'
                    elif user_input[0] in "56":
                        year = '20'
                    elif user_input[0] in "78":
                        year = '21'
                        print(f'{user_input[5:7]}.{user_input[3:5]}.{year}{user_input[1:3]}')
            elif user_choice == '3':
                if int(user_input[7:11]) in range(1, 11):
                    print('Kuuresaare')
                elif '019' >= user_input[7:11] >= '011':
                    print('Tartu')
                elif '160' >= int(user_input[7:11]) >= 151:
                    print('Keila')
                else:
                    print('was not born in Estonia')
            elif user_choice == '4':
                chk1 = [1,2,3,4,5,6,7,8,9,1]
                chk2 = [3,4,5,6,7,8,9,1,2,3]
                result = 0
                for num in range(len(chk1)):
                    print(user_input)
                    result += chk1[num] * int(user_input[num])
                if int(user_input[-1]) == result % 11:
                    print('Code is valid! 1')
                else:
                    result = 0
                    for num in range(len(chk2)):
                        result += chk2[num] * int(user_input[num])
                    if int(user_input[-1]) == result % 11:
                        print('Code is valid! 2')
                    else:
                        print('Code is not valid')

            elif user_choice == '5':
                break
            elif user_choice == '0':
                quit()
            else:
                print('Choice is out of range!')
    # finally:
    #     print('FINALLY')