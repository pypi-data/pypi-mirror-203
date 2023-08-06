import uuid
import hashlib


def get_uuid_offline(username):
    # This Code is translated to Python from the Java Function in the Sourcecode of Minecraft
    offline_uuid = uuid.UUID(hashlib.md5(f"OfflinePlayer:{username}".encode('utf-8')).hexdigest())
    formated_uuid = str(offline_uuid)
    formatted_output = f"Name: {username}\nUUID: {formated_uuid}"
    return formatted_output

