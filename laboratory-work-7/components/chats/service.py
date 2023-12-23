import utils.json_service as json_service
import components.users.service as user


def get_one_by_id(chat_id):
    db = json_service.get_database()

    for elem in db["chats"]:
        if elem["id"] == chat_id:
            return elem

    return {"message": f"Элемент с {chat_id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["chats"]


def update_one_by_id(chat_id, chat):
    db = json_service.get_database()

    for i, elem in enumerate(db["chats"]):
        if elem["id"] == chat_id:
            try:
                elem["name"] = chat["name"]
            except KeyError:
                pass
            try:
                elem["users_id"] = chat["users_id"]
            except KeyError:
                pass

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {chat_id} не найден"}


def delete_one_by_id(chat_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["chats"]):
        if elem["id"] == chat_id:
            candidate = db["chats"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {chat_id} не найден"}


def create_one(chat):
    db = json_service.get_database()

    last_chat_id = get_all()[-1]["id"]
    db["chats"].append({"id": last_chat_id + 1, **chat})

    json_service.set_database(db)


def add_users_to_chats(users, chats):  # добавляем пользователей в чаты - когда создаём пользователя
    for i in get_all():
        for c in range(len(chats)):
            if i["id"] == chats[c]:
                i["users_id"].extend(users)
                update_one_by_id(chats[c], {"users_id": i["users_id"]})

def add_chat_to_users(users, chat):  # добавляем чат в карточки пользователей - когда создаём чат
    for i in user.get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                i["chats_id"].append(chat)
                user.update_one_by_id(users[c], {"chats_id": i["chats_id"]})

def del_user_from_chats(id_user): # когда удаляем пользователя
    for i in get_all():
        if id_user in i["users_id"]:
            i["users_id"].remove(id_user)
            update_one_by_id(i["id"], {"users_id": i["users_id"]})


def del_chat_from_users(id_chat): # когда удаляем чат
    for i in user.get_all():
        if id_chat in i["chats_id"]:
            i["chats_id"].remove(id_chat)
            user.update_one_by_id(i["id"], {"chats_id": i["chats_id"]})

def found_id(name):
    for i in get_all():
        if i["name"] == name:
            return i["id"]

def change_chats_in_users(chats, users):  # изменяем чаты пользователям
    for i in user.get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                user.update_one_by_id(users[c], {"chats_id": chats})  # у пользователей новые чаты
    for t in get_all():
        if t["id"] not in chats:
            for d in range(len(users)):
                if users[d] in t["users_id"]:
                    t["users_id"].remove(users[d])
                    update_one_by_id(t["id"], {"users_id": t["users_id"]})  # удалили пользователей из прошлых чатов