import utils.json_service as json_service
import components.users.service as user


def get_one_by_id(district_id):
    db = json_service.get_database()

    for elem in db["districts"]:
        if elem["id"] == district_id:
            return elem

    return {"message": f"Элемент с {district_id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["districts"]


def update_one_by_id(district_id, district):
    db = json_service.get_database()

    for i, elem in enumerate(db["districts"]):
        if elem["id"] == district_id:
            try:
                elem["name"] = district["name"]
            except KeyError:
                pass
            try:
                elem["users_id"] = district["users_id"]
            except KeyError:
                pass

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {district_id} не найден"}


def delete_one_by_id(district_id):
    db = json_service.get_database()

    for i, elem in enumerate(db["districts"]):
        if elem["id"] == district_id:
            candidate = db["districts"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {district_id} не найден"}


def create_one(district):
    db = json_service.get_database()

    last_district_id = get_all()[-1]["id"]
    db["districts"].append({"id": last_district_id + 1, **district})

    json_service.set_database(db)


def found_id(name):
    for i in get_all():
        if i["name"] == name:
            return i["id"]


def change_district_in_users(id_distr, users):  # изменяем(тк 1 можно) район пользователям
    # (создали район - записали туда пользователей - надо записать этим пользователям соответствующий район)
    for i in user.get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                user.update_one_by_id(users[c], {"district_id": id_distr})  # у пользователей новый район
    for t in get_all():
        if t["id"] != id_distr:
            for d in range(len(users)):
                if users[d] in t["users_id"]:
                    t["users_id"].remove(users[d])
                    update_one_by_id(t["id"], {"users_id": t["users_id"]})  # удалили пользователей из старого района


def add_users_to_district(id_distr, users):  # добавляем пользователей в район
    for i in get_all():
        if i["id"] == id_distr:
            for y in range(len(users)):
                i["users_id"].append(users[y])
            update_one_by_id(id_distr, {"users_id": i["users_id"]})


# def del_users_from_district(id_distr, users):  # удаляем пользователей из района
#     for i in get_all():
#         if i["id"] == id_distr:
#             for y in range(len(users)):
#                 i["users_id"].remove(users[y])
#                 update_one_by_id(id_distr, {"users_id": i["users_id"]})

def del_user_from_district(id_user):  # удаляем пользователя с района
    for i in get_all():
        if id_user in i["users_id"]:
            i["users_id"].remove(id_user)
            update_one_by_id(i["id"], {"users_id": i["users_id"]})


def del_district_from_users(id_distr): # удаляем район (лучше не надо)
    for i in user.get_all():
        if i["district_id"] == id_distr:
            user.update_one_by_id(i["id"], {"district_id": 'None'})

def who_dont_have_district():
    some_users = []
    for t in user.get_all():
        if t["district_id"] == "None":
            some_users.append(t["id"])
    if some_users != []:
        print('Теперь у некоторых пользователей -', some_users, 'нет района :(')

def check_id_for_add(who_id):
    ids = []
    ans =[]
    for i in get_all():
        ids.append(i["id"])
    for c in range(len(who_id)):
        if who_id[c] in ids:
            ans.append(True)
        else:
            ans.append(False)
    if all(ans) == True:
        print("Id существуют")
        return True
    else:
        print('Какого-то Id не существует, попробуйте снова')
        return False