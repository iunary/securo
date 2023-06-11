import os
import tempfile
import unittest

from cryptography.fernet import Fernet

from securo.file_manager import FileManager
from securo.securo import Decryptor, Encryptor


class SecuroTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Fernet.generate_key()

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "plain.txt")
        self.folder_path = os.path.join(self.temp_dir.name, "test_folter")
        os.makedirs(self.folder_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_encrypt_file(self):
        data = b"secret data"
        FileManager.write_file(self.file_path, data)

        encryptor = Encryptor(self.key)
        encryptor.encrypt_file(self.file_path)

        encrypted_data = FileManager.read_file(self.file_path)
        self.assertNotEqual(data, encrypted_data)

    def test_decrypt_file(self):
        data = b"secret data"
        FileManager.write_file(self.file_path, data)

        encryptor = Encryptor(self.key)
        encryptor.encrypt_file(self.file_path)

        decryptor = Decryptor(self.key)
        decryptor.decrypt_file(self.file_path)

        decrypted_data = FileManager.read_file(self.file_path)
        self.assertEqual(decrypted_data, data)

    def test_encrypt_folder(self):
        file1_path = os.path.join(self.folder_path, "file1.txt")
        file2_path = os.path.join(self.folder_path, "file2.txt")

        data1 = b"file 1 secret data"
        data2 = b"file 2 secret data"

        FileManager.write_file(file_path=file1_path, data=data1)
        FileManager.write_file(file_path=file2_path, data=data2)

        encryptor = Encryptor(self.key)
        encryptor.encrypt_folder(self.folder_path)

        encrypted_data1 = FileManager.read_file(file_path=file1_path)
        encrypted_data2 = FileManager.read_file(file_path=file2_path)

        self.assertNotEqual(data1, encrypted_data1)
        self.assertNotEqual(data2, encrypted_data2)

    def test_decrypt_folder(self):
        file1_path = os.path.join(self.folder_path, "file1.txt")
        file2_path = os.path.join(self.folder_path, "file2.txt")

        data1 = b"file 1 secret data"
        data2 = b"file 2 secret data"

        FileManager.write_file(file_path=file1_path, data=data1)
        FileManager.write_file(file_path=file2_path, data=data2)

        encryptor = Encryptor(self.key)
        encryptor.encrypt_folder(folder_path=self.folder_path)

        decryptor = Decryptor(self.key)
        decryptor.decrypt_folder(folder_path=self.folder_path)

        decrypted_data1 = FileManager.read_file(file_path=file1_path)
        decrypted_data2 = FileManager.read_file(file_path=file2_path)

        self.assertEqual(data1, decrypted_data1)
        self.assertEqual(data2, decrypted_data2)


if __name__ == "__main__":
    unittest.main()
