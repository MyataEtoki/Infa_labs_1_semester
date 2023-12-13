import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["chats"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["chats"]


def update_one_by_id(id, chat):
    db = json_service.get_database()

    for i, elem in enumerate(db["chats"]):
        if elem["id"] == id:

            elem["name"] = chat["name"]
            elem["users_id"] = chat["users_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["chats"]):
        if elem["id"] == id:

            candidate = db["chats"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(chat):
    db = json_service.get_database()

    last_chat_id = get_all()[-1]["id"]
    db["chats"].append({"id": last_chat_id + 1, **chat})

    json_service.set_database(db)
