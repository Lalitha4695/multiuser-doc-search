import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_FILE = os.path.join(BASE_DIR, "users", "user_access.json")

def get_user_access(email):
    with open(USER_FILE, 'r') as f:
        access_map = json.load(f)
    return access_map.get(email, [])
