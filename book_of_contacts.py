# Создать книгу контактов. Контакт содержит имя, фамилию и номер телефона.
# Мы можем записывать новый контакт и выводить уже существующий контакт.
# Мы должны проверять что бы в номере телефона были только цифры, а в имени человека и фамилии были только буквы.
# Если имя и фамилия не правильные, то мы пишем в ячейке с именем номер телефона
# Что бы первая буква имени и фамилии начинались с большой буквы.
# Contact Book содержит словари
# Выводить поиск контактов
# Удаление контакта
# Запись файла и считывание из файла
#
#


contact_book = []


def contact_writing(name='', last_name='', phone_number=''):
    dict_1 = {}
    name = big_letter_is(name)
    last_name = big_letter_is(last_name)
    name = name if letter_is(name) else ' '
    last_name = last_name if letter_is(last_name) else ' '
    phone_number = phone_number if number_is(phone_number) else ' '
    name = phone_number if name == ' ' and last_name == ' ' else name
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





if __name__ == '__main__':
    print(contact_writing(name="vasiliy", last_name='Petrov', phone_number='64865685'))
    print(contact_writing(name="Ivan44", last_name='Ivanov44', phone_number='426246424'))
    print(contact_writing(name="Ivan", last_name='ivanov', phone_number='4262d46424'))
    print(finding_of_contact('Ivan'))
    print(deleting_of_contact())
    print(contact_book)

