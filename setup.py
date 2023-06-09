from setuptools import find_packages, setup

VERSION = "1.0.0"

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="securo",
    version=VERSION,
    packages=find_packages(),
    author="Yusuf",
    author_email="contact@yusuf.im",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    install_requires=["cryptography>=3.4.7", "typer>=0.4.0"],
    entry_points={
        "console_scripts": [
            "securo=securo.cli:main",
        ],
    },
    keywords=[
        "securo",
        "encryptor",
        "file encryptor",
        "folder encryptor",
        "encryption",
        "decryption",
        "fernet",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
