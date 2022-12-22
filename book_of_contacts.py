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


contact_book = []


def contact_writing(name='', last_name='', phone_number=''):
    dict_1 = {}
    name = big_letter_is(name)
    last_name = big_letter_is(last_name)
    name = name if letter_is(name) else '-'
    if name == '':
        name = '-'
    last_name = last_name if letter_is(last_name) else '-'
    if last_name == '':
        last_name = '-'
    phone_number = phone_number if number_is(phone_number) else '-'
    if phone_number == '':
        phone_number = '-'
    name = phone_number if name == '-' and last_name == '-' else name
    dict_1.update({'name': name, 'last_name': last_name, 'phone_number': phone_number})
    contact_book.append(dict_1)
    return dict_1


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
            print(f"{contact['name']}, {contact['last_name']}, {contact['phone_number']} \n")
            fh.write(f"{contact['name']}, {contact['last_name']}, {contact['phone_number']} \n")


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

def deleting_of_name():
    try:
        for index, contact in enumerate(contact_book):
            print(f'Контакт номер {index}: {contact}')
        asking = int(input('У какого индекса вы хотите удалить имя? '))
        contact_book[asking]['name'] = '-'
        return contact_book[asking]
    except IndexError:
        return "Контакта с таким индексом не существует"



if __name__ == '__main__':
    print(f"Мы добавляем первый контакт {contact_writing(name='', last_name='Petrov', phone_number='64865685')}")
    print(f"Мы добавляем второй контакт {contact_writing(name='Ivan', last_name='', phone_number='44829413')}")
    print(f"Мы добавляем третий контакт {contact_writing(name='Egor', last_name='Egorov', phone_number='')}")
    print(f"Мы ищем контакт Egor {finding_of_contact(dif_var='Egor')}")
    print(f"Мы удаляем контакт {deleting_of_contact()}")
    print(f"Записываем файл {writing_in_file()}")
    print(f"Читаем из файла {reading_from_file()}")
    print(f'Удаляем номер телефона {deleting_of_phone_number()}')
    print(f"Выводим все контакты {contact_book}")
    print(f"Изменяем номер телефона {editing_of_phone_number()}")
    print(f"Удаляем имя {deleting_of_name()}")


