import utils.json_service as json_service


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


def add_users_to_chat(users, chats): # добавляем пользователей в чаты
    for i in chat.get_all():
        for c in range(len(chats)):
            if i["id"] == chats[c]:
                i["users_id"].extend(users)
                chat.update_one_by_id(chats[c], {"users_id": i["users_id"]})


def add_chats_to_user(who_id, chats): # добавляем чаты в карточку пользователя
    for i in user.get_all():
        if i["id"] == who_id:
            i["chats_id"].extend(chats)
            user.update_one_by_id(who_id, {"chats_id": i["chats_id"]})