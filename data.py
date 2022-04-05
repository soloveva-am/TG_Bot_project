import pickle
user_data ={'ID':['login', 'group number'], }
users = []
'''with open('data.pickle', 'wb') as f:
    # Сериализация словаря data с использованием
    # последней доступной версии протокола.
    pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)'''

def know_user(id):
    '''with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        user_data = pickle.load(f)'''
    if id in user_data.keys():
        return user_data[id]
    return False

def unique_login(login):
    if login in users: return False
    return True

def register(id, username ):
    '''with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        user_data = pickle.load(f)'''
    user_data[id] = [username]
    users.append(username)
    '''with open('data.pickle', 'wb') as f:
        # Сериализация словаря user_data с использованием
        # последней доступной версии протокола.
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)'''

def set_group(id, groupname):
    '''with open('data.pickle', 'rb') as f:
        # Версия протокола определяется автоматически,
        # нет необходимости явно указывать его.
        user_data = pickle.load(f)'''
    user_data[id].append(groupname)
    '''with open('data.pickle', 'wb') as f:
        # Сериализация словаря data с использованием
        # последней доступной версии протокола.
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)'''

