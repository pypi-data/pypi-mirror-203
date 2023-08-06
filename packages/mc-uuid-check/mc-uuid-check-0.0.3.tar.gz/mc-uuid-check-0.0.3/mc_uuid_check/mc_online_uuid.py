# Import Section
import sys
import json
import requests
# --------------


def get_uuid_api(username):
    api_url_base = 'https://api.mojang.com/users/profiles/minecraft/' + username
    response = requests.get(f"{api_url_base}")
    if response.status_code == 404:
        return "Username is not registered, its free or Input is Illegal"
        exit(1)
    else:
        uuid = json.dumps(response.json())
        if uuid[0] == "-":
            uuid = uuid[1:]
        uuid_hyphen = uuid[:8] + '-' + uuid[8:12] + '-' + uuid[12:16] + '-' + uuid[16:20] + '-' + uuid[20:]
        return uuid_hyphen
        #return json.dumps(response.json())

