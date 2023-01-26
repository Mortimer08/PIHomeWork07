menu = [
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'
]


def show_menu():
    print('\nГлавное меню\n')
    for number, item in enumerate(menu):
        print(f'\t{number+1}. {item}')


def user_choice():
    return input('\nВыберите пункт меню: ')


def new_contact() -> dict:
    contact = {}
    contact['Last Name'] = input('Введите фамилию: ')
    contact['First Name'] = input('Введите Имя: ')
    contact['Phone'] = input('Введите номер телефона: ')
    contact['Comment'] = input('Введите комментарий: ')
    return contact

def nothing_delete():
    print('\nНет контактов для удаления:\nФайл не открыт или пуст\n')

def nothing_change():
    print('\nНет контактов для изменения:\nФайл не открыт или пуст\n')


def delete_contact() -> int:
    while True:
        contact_number = input('\nВыберите номер контакта для удаления (0 для выхода): ')
        if contact_number.isdigit():
            return int(contact_number)

def change_contact_choose() -> int:
    while True:
        contact_number = input('\nВыберите номер контакта для изменения (0 для выхода): ')
        if contact_number.isdigit():
            return int(contact_number)

def change_contact(contact_to_change: dict) -> dict:
    changed_lastname = contact_to_change['Last Name']
    changed_firstname = contact_to_change['First Name']
    changed_phone = contact_to_change['Phone']
    changed_comment = contact_to_change['Comment']
    changed_contact = {}
    changed_contact['Last Name'] = input(f'Фамилию {changed_lastname} изменить на: ')
    changed_contact['First Name'] = input(f'Имя {changed_firstname} изменить на: ')
    changed_contact['Phone'] = input(f'Номер телефона {changed_phone} изменить на: ')
    changed_contact['Comment'] = input(f'Комментарий {changed_comment} изменить на: ')
    return changed_contact

def show_contacts(local_recordes: list):
    if len(local_recordes) < 1: 
        print('\nФайл не открыт или пуст\n')
    else:
        for i, line in enumerate(local_recordes):
            line_number = i+1
            print(f'{line_number}.', end = ' ')
            for item in line.values():
                print(f'{item} ', end=' ')
            print()
    print()

def cancel(message):
    print(f'\nОтмена {message}\n')


def warning_exit() -> int:
    print('Изменения не сохранены в файл!\nПодтверждаете выход?')
    print('\t1. Да')
    print('\t2. Нет')
    while True:
        answer = input('\nВыберите: ')
        if answer.isdigit():
            return int(answer)

def warning_openfile() -> int:
    print('В памяти есть записи!\nПри открытии файла записи будут удалены.\nПодтверждаете открытие файла?')
    print('\t1. Да')
    print('\t2. Нет')
    while True:
        answer = input('\nВыберите: ')
        if answer.isdigit():
            return int(answer)

def success(message):
    print(f'\nOK: {message}\n')


def fail(message):
    print(f'\nОшибка {message}\n')
