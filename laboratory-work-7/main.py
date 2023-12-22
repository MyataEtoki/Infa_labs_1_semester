import components.users.service as user
import components.groups.service as group
import components.chats.service as chat
import components.districts.service as districts  # без s не работает (???)
import utils.json_service as json_service

# Нужно взаимодействовать с несколькими сущностями сразу.

def menu():
    operation = input('Выберите операцию: create, update, read, delete\n')
    match operation:
        case 'create':
            object = input('Выберите объект: user, chat, group, district\n')
            match object:
                case 'user':  # хочу шоб добавляешь группу - изменялась и группа етс
                    name = input('Имя:\n')
                    district = int(input('Id района:\n'))
                    email = input('Email:\n')
                    phone = input('Телефон:\n')
                    chats = [int(x) for x in input('Id чатов в которых состоит, через пробел:\n').split()]
                    groups = [int(x) for x in input('Id групп, в которых состоит, через пробел:\n').split()]
                    friends = [int(x) for x in input('Id друзей через пробел: \n').split()]
                    new = {"name": name, "contacts": {"email": email,
                                                      "phone": phone}, "chats_id": chats, "districts_id": district,
                           "friends_users_id": friends, "groups": groups}
                    print(user.create_one(new))
                    print('Успешно создано: ',
                          user.get_one_by_id(user.found_id(name)))  # было бы круто выводить с айдишником
                    '''обновляем связанные сущности: '''
                    add_users_to_district(district, user.found_id(name))
                    chat.add_users_to_chat(user.found_id(name), chats)

                case 'group':
                    name = input('Название:\n')
                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                    new = {"name": name, "users_id": users_id}
                    print(group.create_one(new))
                    print('Успешно создано: ', new)

                case 'district':
                    name = input('Название:\n')
                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                    new = {"name": name, "users_id": users_id}
                    print(districts.create_one(new))
                    print('Успешно создано: ', new)
                case 'chat':
                    name = input('Название:\n')
                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                    new = {"name": name, "users_id": users_id}
                    print(chat.create_one(new))
                    print('Успешно создано: ', new)
                    chat.add_users_to_chat(users_id, new)
        case 'update':
            object = input('Выберите объект: user, chat, group, district\n')
            who_id = int(input('Введите id объекта:\n'))
            match object:
                case 'user':  # можно сделать выбор-цикл типа - чё хошь изменить - это - изменяешь - че хош изменить -... - ничего - конец цикла.
                    name = input('Имя:\n')
                    email = input('Email:\n')
                    phone = input('Телефон:\n')
                    chats = [int(x) for x in input(
                        'Id чатов в которых состоит, через пробел:\n').split()]  # хочу шоб добавляешь чат - изменялся и чат етс
                    groups = [int(x) for x in input('Id групп, в которых состоит, через пробел:\n').split()]
                    district = int(input('Id района:\n'))
                    friends = [int(x) for x in input('Id друзей через пробел: \n').split()]
                    new = {"name": name, "contacts": {"email": email, "phone": phone}, "chats_id": chats,
                           "districts_id": district, "friends_users_id": friends, "groups": groups}

                    print(user.update_one_by_id(who_id, new))
                case 'chat':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    print(chat.update_one_by_id(who_id, new))
                case 'group':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    print(group.update_one_by_id(who_id, new))
                case 'district': #было бы круто - по выбору удалять или добавлять пользователей
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    print(districts.update_one_by_id(who_id, new))
        case 'read':
            object = input('Выберите объект: user, chat, group, district\n')
            who_id = int(input('Введите id объекта:\n'))
            match object:
                case 'user':
                    print(user.get_one_by_id(who_id))
                case 'chat':
                    print(chat.get_one_by_id(who_id))
                case 'group':
                    print(group.get_one_by_id(who_id))
                case 'district':
                    print(districts.get_one_by_id(who_id))
        case 'delete':
            object = input('Выберите объект: user, chat, group, district\n')
            match object:
                case 'user':
                    who_id = int(input('id удаляемого объекта:\n'))
                    print('Успешно удалено: ', user.delete_one_by_id(who_id))
                    # тогда тут удаляешь пользователя - он удаляется из остальных сущностей
                    '''
                    считываем айдишник удал объекта и его тип - ищем в других сущностях запись этого объекта
                    и проверяем есть ли там наш удалённый (пой айди)
                    если есть - удаляем от туда (заменяем на пустоту)
                    '''
                    # с обновлением и добавлением объекта таже тема --> нужна отдельная функция-связка-курьер-почтальон

                case 'chat':
                    who_id = int(input('id удаляемого объекта:\n'))
                    print('Успешно удалено: ', chat.delete_one_by_id(who_id))
                case 'group':
                    who_id = int(input('id удаляемого объекта:\n'))
                    print('Успешно удалено: ', group.delete_one_by_id(who_id))
                case 'district':
                    who_id = int(input('id удаляемого объекта:\n'))
                    print('Успешно удалено: ', districts.delete_one_by_id(who_id))

''' добавить '''



def add_users_to_district(id_distr, users):  # добавляем пользователей в район
    for i in districts.get_all():
        if i["id"] == id_distr:
            for y in range(len(users)):
                i["users_id"].append(users[y])
            districts.update_one_by_id(id_distr, {"users_id": i["users_id"]})

''' изменить (только для района) '''
def change_district_in_users(id_distr, users): # изменяем(тк 1 можно) район пользователям
    # (создали район - записали туда пользователей - надо записать этим пользователям соответствующий район)
    for i in user.get_all():
        for y in range(len(users)):
            if i["id"] == users[y]:
                user.update_one_by_id(users[y], {"district_id": id_distr})


''' удалить '''
def del_users_from_district(id_distr, users): # удаляем пользователей из района
    for i in districts.get_all():
        if i["id"] == id_distr:
            for y in range(len(users)):
                i["users_id"].remove(users[y])
            districts.update_one_by_id(id_distr, {"users_id": i["users_id"]}) #без print работает, но на экран результат не выводится



# print(menu())
