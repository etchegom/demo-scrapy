import hashlib


def hash_value(value: str) -> str:
    """Hash a string value using MD5

    Arguments:
        value {str} -- The string to hash

    Returns:
        str -- The hashed string
    """
    return hashlib.md5(value.encode("utf-8")).hexdigest()
