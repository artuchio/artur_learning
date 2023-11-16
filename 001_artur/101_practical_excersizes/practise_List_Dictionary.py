# 1
# Напишите программу которая сложит все числа в заданном списке
# выведет результат в консоль
nums1 = [5, 6, 92, 47, 12, -18, 33, 8];
total = sum(nums1)
print(total)

# 2
# Напишите программу которая добавит в список edited_names словари
# с двумя парами { "name": "имя с большой буквы", "nameLength": "длина имени"}
names = ['jack', 'sarah', 'mary', 'joey', 'chris', 'samantha'];
edited_names = [];
for name in names:
    capitalised_name = name.capitalize()
    l_name = len(name)
    name_dict = {"name": capitalised_name, "nameLength": l_name, }
    edited_names.append(name_dict)
for entry in edited_names:
    print(entry)

# 3
# Напишите программу которая в список edited_nums добавит словари
# с тремя парами { "number": "само число", "square": "число в квадрпате", "cube": "число в кубе"}
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
edited_nums = [];
for num in nums2:
    num_square = num ** 2  # Вычисляем число в квадрате
    num_cube = num ** 3  # Вычисляем число в кубе
    num_dict = {"number": num, "square": num_square, "cube": num_cube}
    edited_nums.append(num_dict)
for entry in edited_nums:
    print(entry)
# 4
# напишите программу которая выводит в консоль сумму всех
# четных чисел в списке

nums_list = [1, 12, 34, 71, 14, 12, 33, 70, 82, 81, 9, 19, 90];
even_sum = 0
for num in nums_list:
    if num % 2 == 0:
        even_sum += num
    print(f'складываю:', even_sum)


# 5
# напишите программу которая проанализирует данный список и выведет в консоль самую длинную строку

some_strings = ['Star', 'Planet', 'Comet', 'Interstellar', 'Space'];
longest_string = ' '
for string in some_strings:
    if len(string) > len(longest_string):
        longest_string = string
    print(longest_string)
# 6
# напишите программу которая возьмёт из данного списка наименования книг которые вышли в этом году
# и добавит их в новый список

books = [
    {
        'author': 'Jeremy Brook',
        'title': 'My childhood',
        'release': 2023
    },
    {
        'author': 'Samantha Jhones',
        'title': 'Living with ten cats',
        'release': 2020
    },
    {
        'author': 'Bob Summers',
        'title': 'Exploring far space',
        'release': 2021
    },
    {
        'author': 'Bill Brown',
        'title': 'Insects in our garden',
        'release': 2023
    },
    {
        'author': 'Jessica Love',
        'title': 'Programming for begginers',
        'release': 2023
    }
];
latest_books = []
for book in books:
    if book['release'] == 2023:
        latest_books.append(book['title'])
print("LATEST BOOKS IN STORE: ")
for title in latest_books:
    print(title)


# 7
# Напишите функцию которая будет принимать два аргумента (start, end)
# Для каждого числа в диапозоне от start до end будет выводить число
# И Четное оно Или нечетное

def print_even_or_odd(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f'{num} EVEN')
        else:
            print(f'{num} ODD')
start_num = 1
end_num = 10
print_even_or_odd(start_num, end_num)