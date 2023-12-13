import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["districts"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["districts"]


def update_one_by_id(id, district):
    db = json_service.get_database()

    for i, elem in enumerate(db["districts"]):
        if elem["id"] == id:

            elem["name"] = district["name"]
            elem["users_id"] = district["users_id"]
            

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["districts"]):
        if elem["id"] == id:

            candidate = db["districts"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(district):
    db = json_service.get_database()

    last_district_id = get_all()[-1]["id"]
    db["districts"].append({"id": last_district_id + 1, **district})

    json_service.set_database(db)
