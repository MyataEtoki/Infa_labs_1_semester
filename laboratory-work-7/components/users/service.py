import utils.json_service as json_service
import components.groups.service as group
import components.chats.service as chat
import components.districts.service as districts


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

    for i, elem in enumerate(db["users"]):  # пронумировал юзеров (нумер, значение)
        if elem["id"] == user_id:  # ищем нужного юзера
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
                elem["district_id"] = user["district_id"]
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
            candidate = db["users"].pop(i)  # удаляет из массива элемент по(индексу)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {user_id} не найден"}


def found_id(name):
    for i in get_all():
        if i["name"] == name:
            return i["id"]


def create_one(user):
    db = json_service.get_database()

    last_user_id = get_all()[-1]["id"]  # значение последнего существующего айди
    db["users"].append({"id": last_user_id + 1, **user})  # добавляем его в конец

    json_service.set_database(db)

def add_user_to_friends(id_user, friends): # когда создаём пользователя
    for i in get_all():
        for c in range(len(friends)):
            if i["id"] == friends[c]:
                i["friends_users_id"].append(id_user)
                update_one_by_id(friends[c], {"friends_users_id" : i["friends_users_id"]})

def del_user_from_friends(id_user): # когда удаляем пользователя
    for i in get_all():
        if id_user in i["friends_users_id"]:
            i["friends_users_id"].remove(id_user)
            update_one_by_id(i["id"], {"friends_users_id": i["friends_users_id"]})

def change_friends_in_users(friends, users):  # изменяем друзей пользователей
    for i in get_all():
        for c in range(len(users)):
            if i["id"] == users[c]:
                update_one_by_id(users[c], {"friends_users_id": friends})  # у пользователей новые друзья
    for t in get_all():
        if t["id"] not in friends:
            for d in range(len(users)):
                if users[d] in t["friends_users_id"]:
                    t["friends_users_id"].remove(users[d])
                    update_one_by_id(t["id"], {"friends_users_id": t["friends_users_id"]})  # удалили пользователей у прошлых друзей


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