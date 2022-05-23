import pickle
user_data ={'ID':['login', 'group number'], }
users = []
import os.path
if not os.path.exists('data.pickle'):
    with open('data.pickle', 'wb') as f:
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)
else:
    with open ('data.pickle', 'rb') as f:
            user_data = pickle.load(f)

def know_user(id):
    with open('data.pickle', 'rb') as f:
        user_data = pickle.load(f)
    if id in user_data.keys():
        return user_data[id]
    return False

def unique_login(login):
    if login in users: return False
    return True

def register(id, username ):
    with open('data.pickle', 'rb') as f:
        user_data = pickle.load(f)
    user_data[id] = [username]
    users.append(username)
    with open('data.pickle', 'wb') as f:
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)

def set_group(id, groupname):
    with open('data.pickle', 'rb') as f:
        user_data = pickle.load(f)
    user_data[id].append(groupname)
    with open('data.pickle', 'wb') as f:
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)

def delete_user(id):
    with open('data.pickle', 'rb') as f:
        user_data = pickle.load(f)
    k=user_data.pop(id, False)
    with open('data.pickle', 'wb') as f:
        pickle.dump(user_data, f, pickle.HIGHEST_PROTOCOL)
    if k: users.remove(k[0])
    return k