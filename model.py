from pathlib import Path
main_path = Path.cwd()
uni_path = Path('PIHomeWork07','database.txt')
recordes = []
recordes_is_changed = False


def read_db() -> list:
    global recordes
    recordes = []
    with open(uni_path, 'r', encoding='UTF-8') as file:
        file_data = file.readlines()
        for line in file_data:
            record = line.replace('\n', '').split(';')
            recordes.append({'Last Name': record[0], 'First Name': record[1],
                             'Phone': record[2], 'Comment': record[3]})


def save_db() -> list:
    global recordes

    with open(uni_path, 'w', encoding='UTF-8') as file:
        for record in recordes:
            line = ''
            for item in record.values():
                line += item
                line += ';'

            file.write(line+'\n')


def add_contact(contact: dict):
    recordes.append({'Last Name': contact['Last Name'], 'First Name': contact['First Name'],
                     'Phone': contact['Phone'], 'Comment': contact['Comment']})


def delete_contact(contact_number: int):
    recordes.pop(contact_number)


def change_contact(changed_contact_number: int, changed_contact: dict):
    recordes.pop(changed_contact_number)
    recordes.insert(changed_contact_number, changed_contact)
