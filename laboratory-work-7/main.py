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
                case 'user':
                    name = input('Имя:\n')
                    email = input('Email:\n')
                    phone = input('Телефон:\n')
                    chats = input('Id чатов в которых состоит, через пробел:\n').split()
                    groups = input('Id групп, в которых состоит, через пробел:\n').split()
                    district = int(input('Id района:\n'))
                    friends = input('Id друзей через пробел: \n').split()
                    new_user = {"name": name, "contacts": {"email": email,
                                                           "phone": phone}, "chats_id": chats, "districts_id": district,
                                "friends_users_id": friends, "groups": groups}
                    user.create_one(new_user)
                    print(new_user)
                case 'group':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    print(group.create_one(new))
                case 'district':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    districts.create_one(new)
                case 'chat':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    chat.create_one(new)
        case 'update':
            object = input('Выберите объект: user, chat, group, district\n')
            who_id = int(input('Введите id объекта:\n'))
            match object:
                case 'user':  # можно сделать выбор-цикл типа - чё хошь изменить - это - изменяешь - че хош изменить -... - ничего - конец цикла.
                    name = input('Имя:\n')
                    email = input('Email:\n')
                    phone = input('Телефон:\n')
                    chats = input('Id чатов в которых состоит, через пробел:\n').split()
                    groups = input('Id групп, в которых состоит, через пробел:\n').split()
                    district = int(input('Id района:\n'))
                    friends = input('Id друзей через пробел: \n').split()
                    new = {"name": name, "contacts": {"email": email, "phone": phone}, "chats_id": chats,
                           "districts_id": district, "friends_users_id": friends, "groups": groups}
                    user.update_one_by_id(who_id, new)
                case 'chat':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    chat.update_one_by_id(who_id, new)
                case 'group':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    group.update_one_by_id(who_id, new)
                case 'district':
                    name = input('Название:\n')
                    users_id = input('Id пользователей через пробел: \n').split()
                    new = {"name": name, "users_id": users_id}
                    districts.update_one_by_id(who_id, new)
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
                    print(user.delete_one_by_id(who_id))
                case 'chat':
                    who_id = int(input('id удаляемого объекта:\n'))
                    chat.delete_one_by_id(who_id)
                case 'group':
                    who_id = int(input('id удаляемого объекта:\n'))
                    group.delete_one_by_id(who_id)
                case 'district':
                    who_id = int(input('id удаляемого объекта:\n'))
                    districts.delete_one_by_id(who_id)


print(menu())
# print(user.create_one({
#     "name": "Тест Тест",
#     "contacts": {
#         "email": "тест@example.com",
#         "phone": "+333333"
#     },
#     "chats_id": [
#           1,
#           2
#       ]
# }))


# print(user.delete_one_by_id(5))

# print(user.get_all())

# print(user.get_one_by_id(1))

# print(user.update_one_by_id(4, {
#       "name": "Не Смирнова Екатерина",
#       "contacts": {
#           "email": "нет@example.com",
#           "phone": "+1122334455"
#       }}))
