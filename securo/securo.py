"""Securo encryptor and descryptor classes"""
from __future__ import absolute_import

from cryptography.fernet import Fernet

from securo.file_manager import FileManager


class Encryptor:
    """Encryprot class"""

    def __init__(self, key: bytes) -> None:
        """Encryptor init

        Args:
            key (bytes): encryption key
        """
        self.key = key

    def encrypt_file(self, file_path: str) -> None:
        """encrypt file

        Args:
            file_path (str): file path to be encrypted
        """
        fernet = Fernet(key=self.key)
        file_data = FileManager.read_file(file_path=file_path)
        encrypted_data = fernet.encrypt(file_data)
        FileManager.write_file(file_path=file_path, data=encrypted_data)

    def encrypt_folder(self, folder_path: str) -> None:
        """Encrypt folder files

        Args:
            folder_path (str): folder path that contain files to be encrypted
        """
        file_paths = FileManager.list_files_in_folder(folder_path=folder_path)
        for file_path in file_paths:
            self.encrypt_file(file_path=file_path)


class Decryptor:
    """Decryptor class"""

    def __init__(self, key: bytes) -> None:
        """Decryptor init

        Args:
            key (bytes): encryption key
        """
        self.key = key

    def decrypt_file(self, file_path: str) -> None:
        """Decrypt file

        Args:
            file_path (str): file path to be descrypted
        """
        fernet = Fernet(key=self.key)
        encrypted_data = FileManager.read_file(file_path=file_path)
        file_data = fernet.decrypt(encrypted_data)
        FileManager.write_file(file_path=file_path, data=file_data)

    def decrypt_folder(self, folder_path: str) -> None:
        """Descrypt folder files

        Args:
            folder_path (str): folder path that contain the files to be descrypted
        """
        file_paths = FileManager.list_files_in_folder(folder_path=folder_path)
        for file_path in file_paths:
            self.decrypt_file(file_path=file_path)
