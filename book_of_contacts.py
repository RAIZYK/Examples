# Создать книгу контактов. Контакт содержит имя, фамилию и номер телефона.
# Мы можем записывать новый контакт и выводить уже существующий контакт.
# Мы должны проверять что бы в номере телефона были только цифры, а в имени человека и фамилии были только буквы.
# Если имя и фамилия не правильные, то мы пишем в ячейке с именем номер телефона
# Что бы первая буква имени и фамилии начинались с большой буквы.
# Contact Book содержит словари
# Выводить поиск контактов
# Удаление контакта
# Запись файла и считывание из файла
# Если не указано имя, фамилия или номер телефона, то мы ставим прочерк
# Удаление номера телефона
# Изменение номера телефона
# Удаление и изменение для имени и фамилии
# Обращаться к функции через командную строку
# Добавить день рождения контакту
# Считывать из файла все контакты при запуске программы
# Записывать все контакты, когда мы заканчиваем программу


contact_book = []


def contact_writing(name='', last_name='', phone_number='', birthday=''):
    dict_1 = {}
    name = big_letter_is(name)
    last_name = big_letter_is(last_name)
    name = name if letter_is(name) else '-'
    name = filling_of_empty(name)
    last_name = last_name if letter_is(last_name) else '-'
    last_name = filling_of_empty(last_name)
    phone_number = phone_number if number_is(phone_number) else '-'
    phone_number = filling_of_empty(phone_number)
    name = phone_number if name == '-' and last_name == '-' else name
    birthday = filling_of_empty(birthday)
    dict_1.update({'name': name, 'last_name': last_name, 'phone_number': phone_number, 'birthday': birthday})
    contact_book.append(dict_1)
    return dict_1

def filling_of_empty(var):
    if var == '':
        var = '-'
    return var

def find_contacts(val):
    for contact in contact_book:
        if contact.find(val) >= 0:
            print(contact)


def number_is(phone_number):
    try:
        phone_number = int(phone_number)
        return True
    except ValueError:
        return False


def letter_is(name):
    for letter in name:
        if letter.isdigit():
            return False
    return True


def big_letter_is(name):
    if name == '':
        return name
    if name[0] == name[0].upper():
        return name
    else:
        first_letter = name[0].upper()
        return first_letter + name[1:]



def finding_of_contact(dif_var):
    finded_contacts = []
    for contact in contact_book:
        for dif_variable in contact.values():
            if dif_variable == dif_var:
                finded_contacts.append(contact)
                break
    return finded_contacts


def deleting_of_contact():

    while True:
        try:

            for index, contact in enumerate(contact_book):
                print(f'Контакт номер {index}: {contact}')
            inp_index = int(input("Введите индекс контакта, который хотите удалить, если хотите выйти, напишите -1: "))
            if inp_index == -1:
                return("Изменения внесены в базу")
            ind_pop = contact_book.pop(inp_index)
            print(contact_book)
        except ValueError:
            print("Введите цифру")
        except IndexError:
            print("Контакта с таким индексом не существует")


def writing_in_file():
    with open('file1.txt', 'w') as fh:
        for contact in contact_book:
            fh.write(f"{contact['name']}, {contact['last_name']}, {contact['phone_number']}, {contact['birthday']} \n")


def reading_from_file():
    contact_book_from_file = []
    with open('file1.txt', 'r') as fh:
        for contact in fh.readlines():
            contact = contact.replace('\n', '')
            name, last_name, phone_number = contact.split(',')
            contact_book_from_file.append({'name': name, 'last_name': last_name.strip(), 'phone_number': phone_number.strip()})
    return contact_book_from_file

def deleting_of_phone_number():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите удалить номер телефона? '))
        contact_book[asking]['phone_number'] = '-'
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Удалите номер телефона"




def editing_of_phone_number():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите изменить номер телефона? '))
        if contact_book[asking]:
            pass
        new_phone = int(input('Напишите новый номер телефона '))
        contact_book[asking]['phone_number'] = new_phone
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Измените номер телефона"

def deleting_of_name():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите удалить имя? '))
        contact_book[asking]['name'] = '-'
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Удалите имя"

def editing_of_name():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите изменить имя? '))
        if contact_book[asking]:
            pass
        new_name = input('Напишите новое имя ')
        contact_book[asking]['name'] = new_name
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Измените имя"

def deleting_of_last_name():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите удалить фамилию? '))
        contact_book[asking]['last_name'] = '-'
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Удалите фамилию"

def editing_of_last_name():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите изменить фамилию? '))
        if contact_book[asking]:
            pass
        new_last_name = input('Напишите новою фамилию ')
        contact_book[asking]['last_name'] = new_last_name
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Измените фамилию"

def editing_of_birthday():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите изменить День рождения? '))
        if contact_book[asking]:
            pass
        new_birthday = input('Напишите новый День рождения ')
        contact_book[asking]['birthday'] = new_birthday
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Измените день рождения"

def deleting_of_birthday():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите удалить День рождения? '))
        contact_book[asking]['birthday'] = '-'
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"
    except ValueError:
        return "Удалите День рождения"


def main(command, *params):
    if command == 'add':
        name, last_name, phone_number = params
        print({contact_writing(name, last_name, phone_number)})


if __name__ == '__main__':
    print("Существуют такие команды: \n"
          "add - добавить, \n" 
          "delete - удалить, \n"
          "find - найти, \n"
          "show - показать,\n"
          "remove_param - удалить имя, фамилию или номер телефона, \n"
          "edit_param - изменить имя, фамилию или номер телефона. \n"
          "save - сохранить файл \n"
          "load - загрузить файл \n"
          "exit - выход из функции \n")
    contact_book = reading_from_file()
    if reading_from_file() == []:
        print("Нет записанных контактов")

    while True:
        asking_input = input("Введите команду: ").strip()
        if asking_input == 'exit':
            writing_in_file()
            break
        if asking_input == 'save':
            writing_in_file()
        if asking_input == 'load':
            contact_book = reading_from_file()
        if asking_input == 'add':
            name_input = input("Введите имя: ").strip()
            last_name_input = input("Введите фамилию: ").strip()
            phone_number_input = input("Введите номер телефона: ").strip()
            birthday_input = input("Введите день рождения: ").strip()
            contact = contact_writing(name_input, last_name_input, phone_number_input, birthday_input)
            print("Добавлен новый контакт")
            print(f"Имя: {contact['name']}, \nФамилия: {contact['last_name']}, \nНомер телефона: {contact['phone_number']} \nДень Рождения: {contact['birthday']}")
        if asking_input == 'delete':
            deleting_of_contact()
        if asking_input == 'find':
            variable_input = input("Введите переменную (имя, фамилию или номер телефона): ").strip()
            print(finding_of_contact(variable_input))
        if asking_input == 'writing_file':
            contact_writing()
        if asking_input == 'reading_file':
            reading_from_file()
        if asking_input == 'show':
            for index, contact in enumerate(contact_book):
                print(f"Контакт номер {index + 1}")
                print(f"Имя: {contact['name']}, \nФамилия: {contact['last_name']}, \nНомер телефона: {contact['phone_number']}, \nДень рождения: {contact['birthday']}")
        if asking_input == 'remove_param':
            param_input = input("Что вы хотите удалить: имя, фамилию, номер телефона или День рождения? ").strip()
            if param_input == 'name':
                print(deleting_of_name())
            if param_input == 'last_name':
                print(deleting_of_last_name())
            if param_input == 'phone_number':
                print(deleting_of_phone_number())
            if param_input == 'birthday':
                print(deleting_of_birthday())
        if asking_input == 'edit_param':
            param_edit = input("Что вы хотите изменить: имя, фамилию, номер телефона или День рождения? ").strip()
            if param_edit == 'name':
                print(editing_of_name())
            if param_edit == 'last_name':
                print(editing_of_last_name())
            if param_edit == 'phone_number':
                print(editing_of_phone_number())
            if param_edit == "birthday":
                print(editing_of_birthday())







