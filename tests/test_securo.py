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


if __name__ == "__main__":
    unittest.main()
