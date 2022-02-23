import pickle
data ={'LOGIN':['password hash', 'group number']}
with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def in_data(username):
    with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        data = pickle.load(f)
    if username in data.keys:
        return True
    return False

def password_check(username, phash):
    with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        data = pickle.load(f)
    if phash == data[username][0]:
        return True
    return False

def register(username, phash, groupname ):
    with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        data = pickle.load(f)
    data[username] = [phash, groupname]
    with open('data.pickle', 'wb') as f:
        # Сериализация словаря data с использованием
        # последней доступной версии протокола.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
