import utils.json_service as json_service


def get_one_by_id(group_id):
    db = json_service.get_database()

    for elem in db["groups"]:
        if elem["id"] == group_id:
            return elem

    return {"message": f"Элемент с {group_id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["groups"]


def update_one_by_id(group_id, group):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == group_id:

            elem["name"] = group["name"]
            elem["users_id"] = group["users_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {group_id} не найден"}


def delete_one_by_id(group_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == group_id:

            candidate = db["groups"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {group_id} не найден"}


def create_one(group):
    db = json_service.get_database()

    last_group_id = get_all()[-1]["id"]
    db["groups"].append({"id": last_group_id + 1, **group})

    json_service.set_database(db)
