import argparse
import base64
import os

import sys
import getpass

from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


folder = Path(".NOTEBOOK")
##########################################
#Function Definitions
##########################################

def new_file(file_name):
    try:
        with open(f"{folder}/{file_name}.txt", "x") as f:
            pass
        print(f"\n{file_name}.txt has been successfully created.\n")
    except FileExistsError:
        print("\nFile name already taken.\n")
        sys.exit(0)

def encrypt(file_name):

    password = getpass.getpass("\nEnter Password: ")

    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(f"{folder}/{file_name}.txt", "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(f"{folder}/{file_name}.txt", "wb") as f:
        f.write(salt + encrypted)


def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 600000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    return key

def decrypt(file_name, password):
    try:
        with open(f"{folder}/{file_name}.txt", "rb") as f:
            file_data = f.read()

        salt = file_data[:16]
        encrypted_data = file_data[16:]

        key = derive_key(password, salt)
        fernet = Fernet(key)

        decrypted = fernet.decrypt(encrypted_data).decode()

        return decrypted

    except InvalidToken:
        print("\nIncorrect Password.\n")
        sys.exit(0)
                 

def unlock(file_name):
    if Path(f"{folder}/{file_name}.txt").exists():
        try:
            password = getpass.getpass("\nEnter Password: ")

            decrypted = decrypt(file_name, password)

            return decrypted, password

        except FileNotFoundError: 
            print(f"\n{file_name}.txt not found.\n")
            sys.exit(0)

    else:
        print(f"\n{file_name}.txt not found.\n")
        sys.exit(0)

        
def write2(file_name, decrypted_contents, password):
    #Takes new input and appends it to old contents
    print("\nAdd Text\n")
    add_this = input()
    new_contents = decrypted_contents + f"\n{add_this}"

    #Re-encrypts file
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(new_contents.encode())

    # Rewrites whole file
    with open(f"{folder}/{file_name}.txt", "wb") as f:
        f.write(salt + encrypted)


def delete(file_name):
    try:
        os.remove(f"{folder}/{file_name}.txt")
        print("\nFile successfully deleted.\n")
    except FileNotFoundError:
        print(f"\n{file_name} not found.\n")
        sys.exit(0)

def main():
    #Ensures folder where notes ends up in exists.
    folder.mkdir(exist_ok=True)

    #Parses user inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES", description="Encrypted in-terminal notetaking tool.")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--new")
    group.add_argument("--open")
    group.add_argument("--write")
    group.add_argument("--delete")

    args = parser.parse_args()

    #Decision Tree
    if args.new:
        new_file(args.new)
        encrypt(args.new)
    elif args.write:
        decrypted_file, password = unlock(args.write)
        write2(args.write, decrypted_file, password)
    elif args.open:
        decrypted_contents, password = unlock(args.open)
        print(f"\n{decrypted_contents}\n")
    elif args.delete:
        delete(args.delete)
    else:
        return 0

if __name__=="__main__":
    main()
