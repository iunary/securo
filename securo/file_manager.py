"""Securo file manager for reading and writing files"""
import os
from typing import List


class FileManager:
    """File manager class"""

    @staticmethod
    def read_file(file_path: str) -> bytes:
        """Read the content of file and return it as bytes

        Args:
            file_path (str): file path

        Returns:
            bytes: the content of the file as bytes
        """
        with open(file_path, "rb") as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, data: bytes) -> None:
        """Write the given data to a file

        Args:
            file_path (str): file path
            data (bytes): the data to write to the file
        """
        with open(file_path, "wb") as file:
            file.write(data)

    @staticmethod
    def list_files_in_folder(folder_path: str) -> List[str]:
        """List all files in a given folder

        Args:
            folder_path (str): path to the folder

        Returns:
            List[str]: list of file file paths
        """
        file_paths = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
        return file_paths
