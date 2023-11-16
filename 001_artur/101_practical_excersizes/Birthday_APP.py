import csv
from datetime import datetime, date

# Инициализация словаря для хранения дней рождений
birthdays = {}

# Функция для загрузки данных из файла
def load_data():
    try:
        with open('birthdays.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, birthdate_str = row
                try:
                    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
                    birthdays[name] = birthdate
                except ValueError:
                    print(f"Ошибка: Некорректный формат даты для {name} ({birthdate_str}).")
    except FileNotFoundError:
        # Если файл не существует, создаем его
        with open('birthdays.csv', mode='w', newline='') as file:
            pass

# Функция для сохранения данных в файл
def save_data():
    with open('birthdays.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for name, birthdate in birthdays.items():
            writer.writerow([name, birthdate.strftime('%Y-%m-%d')])

# Загрузка данных при запуске программы
load_data()

# Функция для добавления дня рождения и сохранения в CSV файл
def add_person():
    name = input("Введите имя: ")
    birthdate_str = input("Введите день рождения (гггг-мм-дд): ")
    try:
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()
        birthdays[name] = birthdate
        save_data()  # Сохраняем данные в файл сразу после добавления
        print(f"Запись для {name} добавлена и сохранена в файле birthdays.csv.")
    except ValueError:
        print("Ошибка: Некорректный формат даты. Используйте гггг-мм-дд.")


# Функция для просмотра дня рождения
def view_birthdate():
    name = input("Введите имя, чтобы узнать день рождения: ")
    if name in birthdays:
        birthdate = birthdays[name]
        print(f"{name} родился {birthdate.strftime('%Y-%m-%d')}")

        today = date.today()
        next_birthday = date(today.year, birthdate.month, birthdate.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

        time_until_birthday = datetime.combine(next_birthday, datetime.min.time()) - datetime.combine(today,
                                                                                                      datetime.min.time())
        days_until_birthday = time_until_birthday.days


        print(f"До следующего дня рождения осталось: {days_until_birthday} дней ")
    else:
        print(f"Запись для {name} не найдена.")


# Функция для просмотра всех дней рождений
def list_all_birthdates():
    if birthdays:
        print("Дни рождений:")
        for name, birthdate in birthdays.items():
            print(f"{name}: {birthdate.strftime('%Y-%m-%d')}")
    else:
        print("Список дней рождений пуст.")


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить дни рождения")
    print("2. Посмотреть конкретную запись")
    print("3. Посмотреть все записи")
    print("4. Выйти из программы")
    choice = input("Выберите действие (1/2/3/4): ")

    if choice == '1':
        add_person()
    elif choice == '2':
        view_birthdate()
    elif choice == '3':
        list_all_birthdates()
    elif choice == '4':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
