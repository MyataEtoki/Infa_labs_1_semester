import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["users"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["users"]


def update_one_by_id(id, user):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]): # пронумировал юзеров (нумер, значение)
        if elem["id"] == id: # ищем нужного юзера

            elem["name"] = user["name"] # изменяем параметры на введённые
            elem["contacts"] = user["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["users"]):
        if elem["id"] == id:

            candidate = db["users"].pop(i) # удаляет из массива элемент по(индексу)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(user):
    db = json_service.get_database()

    last_user_id = get_all()[-1]["id"] # значение последнего существующего айди
    db["users"].append({"id": last_user_id + 1, **user}) # добавляем его в конец

    json_service.set_database(db)
