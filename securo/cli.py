"""Securo cli"""
from __future__ import absolute_import

import os

import typer
from cryptography.fernet import InvalidToken

from securo.securo import Decryptor, Encryptor
from securo.utils import get_encryption_key

app = typer.Typer(no_args_is_help=True)


@app.command(help="encrypt a file or files in a folder")
def encrypt(path: str) -> None:
    """encrypt command

    Args:
        path (str): file or folder to be encrypted
    """
    key = get_encryption_key()
    encryptor = Encryptor(key=key)
    if os.path.isfile(path):
        encryptor.encrypt_file(path)
    elif os.path.isdir(path):
        encryptor.encrypt_folder(path)
    else:
        typer.echo(f"invalid file or folder {path}", err=True)


@app.command(help="decrypt a file or files in a folder")
def decrypt(path: str) -> None:
    """Decrypt command

    Args:
        path (str): file or folder to be descrypted
    """
    key = get_encryption_key()
    decryptor = Decryptor(key=key)
    try:
        if os.path.isfile(path):
            decryptor.decrypt_file(path)
        elif os.path.isdir(path):
            decryptor.decrypt_folder(path)
        else:
            typer.echo(f"invalid file or folder {path}", err=True)
    except InvalidToken:
        typer.echo("invalid token", err=True)


def main():
    """Entrypoint function"""
    try:
        app()
    except KeyboardInterrupt:
        typer.echo("Operation interrupted key user", err=True)


if __name__ == "__main__":
    main()
