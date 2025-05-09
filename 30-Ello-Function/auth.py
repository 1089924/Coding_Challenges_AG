# auth.py

# This is your fake user database (temporary for now)
users = {
    "Bartholomew": "Apple",
    "George": "Banana",
    "Jeff": "Cheery",
    "Sam": "Plum",
    "Kiea": "Peach"
}

def add_user(username, password):
    if username in users:
        return False  # User already exists
    users[username] = password
    return True

def check_login(username, password):
    return users.get(username) == password
