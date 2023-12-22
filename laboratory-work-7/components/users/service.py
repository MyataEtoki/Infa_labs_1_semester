import utils.json_service as json_service


def get_one_by_id(user_id):
    db = json_service.get_database()

    for elem in db["users"]:
        if elem["id"] == user_id:
            return elem

    return {"message": f"Элемент с {user_id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["users"]


def update_one_by_id(user_id, user):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]): # пронумировал юзеров (нумер, значение)
        if elem["id"] == user_id: # ищем нужного юзера
            # изменяем параметры на введённые
            try:
                elem["name"] = user["name"]
            except KeyError:
                pass
            try:
                elem["contacts"] = user["contacts"]
            except KeyError:
                pass
            try:
                elem["districts_id"] = user["districts_id"]
            except KeyError:
                pass
            try:
                elem["friends_users_id"] = user["friends_users_id"]
            except KeyError:
                pass
            try:
                elem["chats_id"] = user["chats_id"]
            except KeyError:
                pass
            try:
                elem["groups_id"] = user["groups_id"]
            except  KeyError:
                pass

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {user_id} не найден"}


def delete_one_by_id(user_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        if elem["id"] == user_id:

            candidate = db["users"].pop(i) # удаляет из массива элемент по(индексу)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {user_id} не найден"}

def found_id(name):
    for i in get_all():
        if i["name"] == name:
            return i["id"]

def create_one(user):
    db = json_service.get_database()

    last_user_id = get_all()[-1]["id"] # значение последнего существующего айди
    db["users"].append({"id": last_user_id + 1, **user}) # добавляем его в конец

    json_service.set_database(db)



