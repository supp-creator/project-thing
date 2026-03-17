import argparse
import base64
import cryptography
import os
from pathlib import Path

#Declaration of global variables
command-menu = "" #Type in list of commands.
folder = Path("NOTEBOOK")
security = "locked"

#def
##########################################
#Function Definitions
##########################################

#Function to create a new file; must check if it exists first.
def new_file():


#Define a function to encrypt a specific file.
#Needs overhaul
def encrypt():
    data = ""
    with open(f"folder/{file_name}.txt", "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)



def open_file():
    try:
        with open(f"NOTEBOOK/{file_name}.txt", "r") as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("File does not exists O_O")


def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            lengh = 32,
            salt = salt,
            iterations = 600000,
            )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))



#Define a function to decrypt a specific file.
def decrypt():


#Define a function that prompts user for password and decrypts the chosen file.
#Function must use decrpyt() function
def unlock():
    print("Enter Password...")
    passwd = input()

    decrypt()


def write2():
    if security == "locked":
        print("Can't write to this file...Unlock first...")
    else:
        try:
            with open(f"folder/{file_name}.txt", "a") as f:
                print(r"Add something. (If you want a new line, append a '\n' at the end"))
                add_this = input()
                f.write(add_this)
        except FileNotFoundError:
            print("File doesn't exist...Create it first...")

#Define a function to delete a specific file.
def delete():
    delete_this_file = Path(folder/{args.delete})
    try:
        os.remove(delete_this_file)
    except FileNotFoundError:
        print("File does not exist O_O")



def main():
    # Creates a folder to store all files, makes one if it doesn't exit yet.
    folder.mkdir(exist_ok=True)

    #Parses user inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--new", required=True)
    group.add_argument("--open", required=True)
    group.add_argument("--write", required=True)
    group.add_argument("--delete", required=True)

    args = parser.parse_args()

    #Decision Tree
    if args.new:
        new_file(args.new)
        encrypt(args.new)
    elif args.write:
        unlock(args.write)
        security = "unlocked"
        write2(args.write)
    elif args.open:
        unlock(args.open)
        open_file(args.open)
    elif args.delete:
        delete_file(args.delete)
    else:
        print(comand-menu)

if __name__== "__main__":
    main()
