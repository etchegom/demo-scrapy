import hashlib

import extruct
import requests

from w3lib.html import get_base_url


def hash_value(value: str) -> str:
    """Hash a string value using MD5

    Arguments:
        value {str} -- The string to hash

    Returns:
        str -- The hashed string
    """
    return hashlib.md5(value.encode("utf-8")).hexdigest()


def extract_metadata(url: str) -> dict:
    """Extract metadata using extruct 3rdparty tool.

    Arguments:
        url {str} -- The URL to analyze

    Returns:
        dict -- Metadata extraction
    """

    r = requests.get(url)
    base_url = get_base_url(r.text, r.url)
    return extruct.extract(r.text, base_url=base_url)
