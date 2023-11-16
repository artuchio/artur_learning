import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def top_countries(data, column_index, num_countries):
    if column_index < 4 or column_index >= len(data[0]):
        print("Выбран некорректный столбец.")
        return

    # Извлекаем данные из выбранного столбца и создаем список кортежей (значение, индекс)
    column_data = [(row[column_index], index) for index, row in enumerate(data)]

    # Удаляем строки с текстовыми значениями
    column_data = [(value, index) for value, index in column_data if value.replace('.', '', 1).replace('-', '', 1).replace(',', '', 1).isdigit()]

    # Сортируем по выбранному столбцу
    column_data.sort(key=lambda x: float(x[0]), reverse=True)

    # Выводим топ N стран
    print(f"Топ {num_countries} стран по столбцу {data[0][column_index]}:")
    for i in range(min(num_countries, len(column_data))):
        index = column_data[i][1]
        print(f"{data[index][1]}: {column_data[i][0]}")

if __name__ == '__main__':
    filename = '2019.csv'
    data = load_data(filename)

    while True:
        print("\nМеню:")
        print("1. Вывести топ стран по выбранному столбцу")
        print("2. Выход")
        print('1.GDP per capita\n')
        print('2.Social support\n')
        print('3.Healthy life expectancy\n')
        print('4.Freedom to make life choices\n')
        print('5.Generosity\n')
        print('6.Perceptions of corruption\n')
        print('0. Exit\n''-->')
        choice = input("Выберите действие (1/2): ")

        if choice == '1':
            column_index = int(input("Введите номер столбца для сортировки (от 4 и далее): "))

            num_countries = int(input("Введите количество стран для вывода: "))
            if num_countries > len(data) - 1:
                print("Ошибка: Запрашиваемое количество стран больше, чем есть в таблице.")
            else:
                top_countries(data, column_index, num_countries)
        elif choice == '2':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

#######################################################################################################################
# import csv
#
# with open('2019.csv', 'r') as file:
#     data = csv.reader(file)
#     headers = next(data)
#     data = list(data)
#
# top = 10
# column = 3
#
# # indexes = list(enumerate(headers)
# # print(list(indexes))
#
#
# def sort_by_column(column, top):
#     data_copy = data.copy()
#     data_copy.sort(key=lambda x: x[column])
#
#     result = []
#     while len(result) < top:
#         result.append(data_copy.pop())
#     return result
#
# for res in sort_by_column(column, top):
#
#     print(res)
# while True:
#     user_choice = input('1.GDP per capita\n'
#                         '2.Social support\n'
#                         '3.Healthy life expectancy\n'
#                         '4.Freedom to make life choices\n'
#                         '5.Generosity\n'
#                         '6.Perceptions of corruption\n'
#                         '0. Exit\n'
#                         '-->')
#
#     if user_choice == '1':
#         print(sort_by_column(3, top))
#     elif user_choice == '2':
#         print(sort_by_column(4, top))
#     elif user_choice == '3':
#         print(sort_by_column(5, top))
#     elif user_choice == '4':
#         print(sort_by_column(6, top))
#     elif user_choice == '5':
#         print(sort_by_column(7, top))
#     elif user_choice == '6':
#         print(sort_by_column(8, top))
#     elif user_choice == '7':
#         pass
#     elif user_choice == '0':
#         print('goodbye')
#         break
#     else:
#         print('Choice out of range')
