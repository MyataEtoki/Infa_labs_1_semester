import components.users.service as user
import components.groups.service as group
import components.chats.service as chat
import components.districts.service as districts  # без s не работает (???)


def menu():
    operation = input('Выберите операцию: create, update, read, delete\n')
    check = False
    match operation:
        # СОЗДАНИЕ
        case 'create':
            object = input('Выберите объект: user, chat, group, district\n')
            match object:
                case 'user':
                    name = input('Имя:\n')
                    print('Существующие районы:', districts.get_all())
                    while check == False:
                        district = int(input('Id района:\n'))
                        check = districts.check_id_for_add([district])
                    check = False
                    email = input('Email:\n')
                    phone = input('Телефон:\n')
                    print('Существующие чаты:', chat.get_all())
                    while check == False:
                        chats = [int(x) for x in input('Id чатов в которых состоит, через пробел:\n').split()]
                        check = chat.check_id_for_add(chats)
                    check = False
                    print('Существующие группы:', group.get_all())
                    while check == False:
                        groups = [int(x) for x in input('Id групп, в которых состоит, через пробел:\n').split()]
                        check = group.check_id_for_add(groups)
                    check = False
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        friends = [int(x) for x in input('Id друзей через пробел: \n').split()]
                        check = user.check_id_for_add(friends)
                    new = {"name": name, "contacts": {"email": email,
                                                      "phone": phone}, "chats_id": chats, "district_id": district,
                           "friends_users_id": friends, "groups_id": groups}
                    print(user.create_one(new))
                    print('Успешно создано: ', user.get_one_by_id(user.found_id(name)))
                    '''обновляем связанные сущности: '''
                    districts.add_users_to_district(district, [user.found_id(name)])
                    chat.add_users_to_chats([user.found_id(name)], chats)
                    group.add_users_to_groups([user.found_id(name)], groups)
                    user.add_user_to_friends(user.found_id(name), friends)

                case 'group':
                    name = input('Название:\n')
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                        check = user.check_id_for_add(users_id)
                    new = {"name": name, "users_id": users_id}
                    print(group.create_one(new))
                    print('Успешно создано: ', group.get_one_by_id(group.found_id(name)))
                    group.add_group_to_users(users_id, group.found_id(name))
                case 'district':
                    name = input('Название:\n')
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                        check = user.check_id_for_add(users_id)
                    new = {"name": name, "users_id": users_id}
                    print(districts.create_one(new))
                    print('Успешно создано: ', districts.get_one_by_id(districts.found_id(name)))
                    # districts.add_users_to_district(districts.found_id(name), users_id) # а зачем?
                    districts.change_district_in_users(districts.found_id(name), users_id)
                case 'chat':
                    name = input('Название:\n')
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                        check = user.check_id_for_add(users_id)
                    new = {"name": name, "users_id": users_id}
                    print(chat.create_one(new))
                    print('Успешно создано: ', chat.get_one_by_id(chat.found_id(name)))
                    chat.add_chat_to_users(users_id, chat.found_id(name))
        # ОБНОВЛЕНИЕ
        case 'update':
            object = input('Выберите объект: user, chat, group, district\n')
            check = False
            match object:
                case 'user':
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = user.check_id_for_add(who_id)
                    check = False
                    while True:
                        choice = input('Что вы хотите изменить: name, contacts, chats, groups, district, friends ?\n'
                                       'Напишите "end", чтобы завершить\n')
                        match choice:
                            case 'name':
                                name = input('Имя:\n')
                                print(user.update_one_by_id(who_id, {"name": name}))
                            case 'contacts':
                                email = input('Email:\n')
                                phone = input('Телефон:\n')
                                print(user.update_one_by_id(who_id, {"contacts": {"email": email, "phone": phone}}))
                            case 'chats':
                                print('Существующие чаты:', chat.get_all())
                                while check == False:
                                    chats = [int(x) for x in
                                             input('Id чатов в которых состоит, через пробел:\n').split()]
                                    check = chat.check_id_for_add(chats)
                                check = False
                                print(user.update_one_by_id(who_id, {"chats_id": chats}))
                                chat.change_chats_in_users(chats, [who_id])
                                chat.add_users_to_chats([who_id], chats)
                            case 'groups':
                                print('Существующие группы:', group.get_all())
                                while check == False:
                                    groups = [int(x) for x in
                                              input('Id групп, в которых состоит, через пробел:\n').split()]
                                    check = group.check_id_for_add(groups)
                                check = False
                                print(user.update_one_by_id(who_id, {"groups_id": groups}))
                                group.change_groups_in_users(groups, [who_id])  # изменяет карточку пользователя
                                group.add_users_to_groups([who_id], groups)  # изменяет карточки групп
                            case 'district':
                                print('Существующие районы:', districts.get_all())
                                while check == False:
                                    district = int(input('Id района:\n'))
                                    check = districts.check_id_for_add([district])
                                check = False
                                print(user.update_one_by_id(who_id, {"districts_id": district}))
                                districts.change_district_in_users(district, [who_id])
                                districts.add_users_to_district(district, [who_id])
                            case 'friends':
                                print('Существующие пользователи:', user.get_all())
                                friends = [int(x) for x in input('Id друзей через пробел: \n').split()]
                                print(user.update_one_by_id(who_id, {"friends_users_id": friends}))
                                user.change_friends_in_users(friends, [who_id])
                                user.add_user_to_friends(who_id, friends)
                            case 'end':
                                break

                case 'chat':
                    print('Существующие чаты:', chat.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = chat.check_id_for_add(who_id)
                    check = False
                    while True:
                        choice = input('Что вы хотите изменить: name, users_id ?\nНапишите "end", чтобы завершить\n')
                        match choice:
                            case 'name':
                                name = input('Название:\n')
                                print(chat.update_one_by_id(who_id, {"name": name}))
                            case 'users_id':
                                print('Существующие пользователи:', user.get_all())
                                while check == False:
                                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                                    check = user.check_id_for_add(users_id)
                                print(chat.update_one_by_id(who_id, {"users_id": users_id}))
                                chat.del_chat_from_users(who_id)
                                chat.add_chat_to_users(users_id, who_id)
                            case 'end':
                                break

                case 'group':
                    print('Существующие группы:', group.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = group.check_id_for_add(who_id)
                    check = False
                    while True:
                        choice = input('Что вы хотите изменить: name, users_id ?\nНапишите "end", чтобы завершить\n')
                        match choice:
                            case 'name':
                                name = input('Название:\n')
                                print(group.update_one_by_id(who_id, {"name": name}))
                            case 'users_id':
                                print('Существующие пользователи:', user.get_all())
                                while check == False:
                                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                                    check = user.check_id_for_add(users_id)
                                print(group.update_one_by_id(who_id, {"users_id": users_id}))
                                group.del_group_from_users(who_id)
                                group.add_group_to_users(users_id, who_id)
                            case 'end':
                                break
                case 'district':
                    print('Существующие районы:', districts.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = districts.check_id_for_add(who_id)
                    check = False
                    while True:
                        choice = input('Что вы хотите изменить: name, users_id ?\nНапишите "end", чтобы завершить\n')
                        match choice:
                            case 'name':
                                name = input('Название:\n')
                                print(districts.update_one_by_id(who_id, {"name": name}))
                            case 'users_id':
                                print('Существующие пользователи:', user.get_all())
                                while check == False:
                                    users_id = [int(x) for x in input('Id пользователей через пробел: \n').split()]
                                    check = user.check_id_for_add(users_id)
                                print(districts.update_one_by_id(who_id, {"users_id": users_id}))
                                districts.del_district_from_users(who_id)
                                districts.change_district_in_users(who_id, users_id)
                                districts.who_dont_have_district()
                            case 'end':
                                break
        # ЧТЕНИЕ
        case 'read':
            object = input('Выберите объект: user, chat, group, district\n')
            check = False
            match object:
                case 'user':
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = user.check_id_for_add(who_id)
                    print(user.get_one_by_id(who_id))
                case 'chat':
                    print('Существующие чаты:', chat.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = chat.check_id_for_add(who_id)
                    print(chat.get_one_by_id(who_id))
                case 'group':
                    print('Существующие группы:', group.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = group.check_id_for_add(who_id)
                    print(group.get_one_by_id(who_id))
                case 'district':
                    print('Существующие районы:', districts.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = districts.check_id_for_add(who_id)
                    print(districts.get_one_by_id(who_id))
        # УДАЛЕНИЕ
        case 'delete':
            object = input('Выберите объект: user, chat, group, district\n')
            check = False
            match object:
                case 'user':
                    print('Существующие пользователи:', user.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = user.check_id_for_add(who_id)
                    districts.del_user_from_district(who_id)
                    group.del_user_from_groups(who_id)
                    chat.del_user_from_chats(who_id)
                    user.del_user_from_friends(who_id)
                    print('Успешно удалено: ', user.delete_one_by_id(who_id))

                case 'chat':
                    print('Существующие чаты:', chat.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = chat.check_id_for_add(who_id)
                    chat.del_chat_from_users(who_id)
                    print('Успешно удалено: ', chat.delete_one_by_id(who_id))
                case 'group':
                    print('Существующие группы:', group.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = group.check_id_for_add(who_id)
                    group.del_group_from_users(who_id)
                    print('Успешно удалено: ', group.delete_one_by_id(who_id))
                case 'district':
                    print('Существующие районы:', districts.get_all())
                    while check == False:
                        who_id = int(input('Введите id объекта:\n'))
                        check = districts.check_id_for_add(who_id)
                    districts.del_district_from_users(who_id)
                    districts.who_dont_have_district()
                    print('Успешно удалено: ', districts.delete_one_by_id(who_id))


print(menu())
