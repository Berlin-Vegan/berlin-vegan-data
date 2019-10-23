from django.utils.crypto import get_random_string


def get_random_string_32():
    return get_random_string(
        length=32, allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789"
    )
