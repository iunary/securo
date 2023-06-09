# securo

A Python CLI package that provides functionality to encrypt and decrypt files or folders using symmetric encryption.

## Features

- Encrypt a file or folder
- Decrypt a file or folder
- Uses the Fernet encryption algorithm from the `cryptography` library

## Installation

Install the package:

```shell
$ pip install securo
```

## Usage

Encrypt a file:
```shell
$ securo encrypt /path/to/file.txt
```

Encrypt a folder:
```shell
$ securo encrypt /path/to/folder
```

Decrypt a file:
```shell
$ securo decrypt /path/to/file.txt
```

Decrypt a folder:
```shell
$ securo decrypt /path/to/folder
```

Note: When prompted, enter the encryption key. The same key should be used for encryption and decryption.