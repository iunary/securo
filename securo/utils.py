"""Securo utils"""
import base64
import getpass
import hashlib


def secure_key(key: bytes) -> bytes:
    """secure key

    Args:
        key (bytes): encryption key

    Returns:
        bytes: secured key for fernet
    """
    hlib = hashlib.md5()
    hlib.update(key)
    return hlib.hexdigest().encode()


def get_encryption_key() -> str:
    """Get the encryption key

    Returns:
        str: the encryption key
    """
    key = getpass.getpass(prompt="Enter the encryption key: ")
    return base64.urlsafe_b64encode(secure_key(key=key.encode()))
