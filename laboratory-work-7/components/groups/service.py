import utils.json_service as json_service
import components.users.service as user


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
            try:
                elem["name"] = group["name"]
            except KeyError:
                pass
            try:
                elem["users_id"] = group["users_id"]
            except KeyError:
                pass

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


def add_users_to_groups(users, groups):  # добавляем пользователей в группы
    for i in get_all():
        for c in range(len(groups)):
            if i["id"] == groups[c]:
                i["users_id"].extend(users)
                update_one_by_id(groups[c], {"users_id": i["users_id"]})


def add_group_to_users(users, id_group):  # добавляем группу в карточки пользователей
    for i in user.get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                i["groups_id"].append(id_group)
                user.update_one_by_id(users[c], {"groups_id": i["groups_id"]})

def del_user_from_groups(id_user): # когда удаляем пользователя
    for i in get_all():
        if id_user in i["users_id"]:
            i["users_id"].remove(id_user)
            update_one_by_id(i["id"], {"users_id": i["users_id"]})


def del_group_from_users(id_group): # когда удаляем группу
    for i in user.get_all():
        if id_group in i["groups_id"]:
            i["groups_id"].remove(id_group)
            user.update_one_by_id(i["id"], {"groups_id": i["groups_id"]})

def found_id(name):
    for i in get_all():
        if i["name"] == name:
            return i["id"]

def change_groups_in_users(groups, users):  # изменяем группы пользователям
    for i in user.get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                user.update_one_by_id(users[c], {"groups_id": groups})  # у пользователей новые группы
    for t in get_all():
        if t["id"] not in groups:
            for d in range(len(users)):
                if users[d] in t["users_id"]:
                    t["users_id"].remove(users[d])
                    update_one_by_id(t["id"], {"users_id": t["users_id"]})  # удалили пользователей из прошлых групп