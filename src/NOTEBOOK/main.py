import argparse
import base64
import cryptography
import os
from pathlib import Path

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


#Declaration of global variables
command_menu = "testing..." #Type in list of commands.
folder = Path("NOTEBOOK")
security = "locked"

##########################################
#Function Definitions
##########################################

#Function to create a new file; must check if it exists first.
def new_file(file_name):
    try:
        with open(f"{file_name}.txt", "x") as f:
            pass
        print(f"\nFile: {file_name}.txt has been successfully created.\n")
    except FileExistsError:
        print("File name already taken...Pick a new one...")

#Define a function to encrypt a specific file.
def encrypt(file_name):

    password = input()

    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(f"{file_name}", "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as f:
        f.write(salt + encrypted)


def open_file(file_name):
    try:
        with open(f"{file_name}.txt", "r") as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("File does not exists...")


def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 600000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

#Define a function to decrypt a specific file.
def decrypt(file_name, password):

    with open(f"{file_name}", "rb") as f:
        file_data = f.read()

    salt = file_data[:16]
    encrypted_data = file_data[16:]

    key = derive_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted_data)
        return decrypted.decode()
    
    except:
        print("Incorrect Password.")
        return None

#Define a function that prompts user for password and decrypts the chosen file.
#Function must use decrpyt() function
def unlock(file_name):
    password = input()

    decrypted = decrypt(file_name, password)
    if decrypted is not None:
        global security
        security = "unlocked"

        return decrypted
    else:
        return None

def write2(file_name):
    if security == "locked":
        print("Can't write to this file...Unlock it first...")
    else:
        try:
            with open(f"{file_name}.txt", "a") as f:

                print(r"Add something. (If you want a new line, append a '\n' at the end")
                add_this = input()
                f.write(add_this)
        except FileNotFoundError:
            print(f"The file: {file_name} doesn't exist.")

#Define a function to delete a specific file.
def delete(file_name):
    delete_this_file = f"{file_name}"
    try:
        os.remove(delete_this_file)
    except FileNotFoundError:
        print("\nFile not found...\n")



def main():
    # Creates a folder to store all files, makes one if it doesn't exit yet.

    #Parses user inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--new")
    group.add_argument("--open")
    group.add_argument("--write")
    group.add_argument("--delete")

    args = parser.parse_args()

    #Decision Tree
    if args.new:
        new_file(args.new)
        print("\nEnter Password for this file:\n")
        encrypt(args.new)
    elif args.write:
        print("Enter Password:")
        unlock(args.write)
        global security
        security = "unlocked"
        write2(args.write)
    elif args.open:
        unlock(args.open)
        open_file(args.open)
    elif args.delete:
        delete(args.delete)
        print("\nFile successfully deleted...\n")
    else:
        print(command_menu)

if __name__== "__main__":
    main()
