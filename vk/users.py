from config import DEFAULT_USERS

known_users = set(DEFAULT_USERS)


def add_user(user_id: int):
    known_users.add(user_id)


def get_all_users():
    return known_users