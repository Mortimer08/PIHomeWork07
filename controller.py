import model
import view


def start():
    while True:
        view.show_menu()
        menu_item = view.user_choice()
        print()
        if menu_item.isdigit:
            if menu_item == '1':
                try:
                    view.show_contacts(model.recordes)
                    view.success('')
                except:
                    view.fail('при отображении контактов')
            elif menu_item == '2':
                try:
                    if len(model.recordes) > 0:
                        answer = view.warning_openfile()
                        if answer == 1:
                            model.read_db()
                            view.success('Файл открыт')
                    model.read_db()
                    view.success('Файл открыт')
                except:
                    view.fail('при открытии файла')
            elif menu_item == '3':
                try:

                    model.save_db()
                    view.success('Файл сохранён')
                    model.recordes_is_changed = False
                except:
                    view.fail('При сохранении файла')
            elif menu_item == '4':
                try:
                    new_contact = view.new_contact()
                    model.add_contact(new_contact)
                    view.success('Контакт создан')
                    model.recordes_is_changed = True
                except:
                    view.fail('при создании контакта')
            elif menu_item == '5':
                try:
                    if len(model.recordes) < 1:
                        view.nothing_change()
                    else:
                        change_contact_number = view.change_contact_choose() - 1
                        if change_contact_number > 0:
                            changed_contact = view.change_contact(
                                model.recordes[change_contact_number])
                            model.change_contact(
                                change_contact_number, changed_contact)

                            view.success('Контакт изменён')
                            model.recordes_is_changed = True
                        else:
                            view.cancel('изменения контакта')
                except:
                    view.fail('при изменении контакта')
            elif menu_item == '6':
                try:
                    if len(model.recordes) < 1:
                        view.nothing_delete()
                    else:
                        view.show_contacts(model.recordes)
                        delete_contact = view.delete_contact() - 1
                        if delete_contact > 0:
                            model.delete_contact(delete_contact)
                            view.success('Контакт удалён')
                            model.recordes_is_changed = True
                        else:
                            view.cancel('удаления контакта')
                except:
                    view.fail('при удалении контакта')

            elif menu_item == '7':
                if model.recordes_is_changed:
                    answer = view.warning_exit()
                    if answer == 1:
                        exit()
                else:
                    exit()
