import argparse
import base64
import cryptography
import os
from pathlib import Path

#Declaration of global variables
command_menu = "testing..." #Type in list of commands.
folder = Path("NOTEBOOK")
security = "locked"

##########################################
#Function Definitions
##########################################

#Function to create a new file; must check if it exists first.
#def new_file():


#Define a function to encrypt a specific file.
#Needs overhaul
def encrypt(file_name, password):
    file_path = folder / f"{file_name}.txt"

    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(salt + encrypted)


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
        lenght = 32,
        salt = salt,
        iterations = 600000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key



#Define a function to decrypt a specific file.
def decrypt(file_name, password):
    file_path = folder / f"{file_name}.txt"

    with open(file_path, "rb") as f:
        file_data = f.read()

    salt = file_data[:16]
    encrypted_data = file_data[16:]
    key = derive_key(password, salt)
    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted_data)
        return decrypted.decode()
    
    except:
        print("Decryption Failed - Wrong Password!")
        return None

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
                print(r"Add something. (If you want a new line, append a '\n' at the end")
                add_this = input()
                f.write(add_this)
        except FileNotFoundError:
            print("File doesn't exist...Create it first...")

#Define a function to delete a specific file.
def delete(file):
    delete_this_file = Path(folder/file)
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
        unlock(args.write)
        security = "unlocked"
        write2(args.write)
    elif args.open:
        unlock(args.open)
        open_file(args.open)
    elif args.delete:
        delete(args.delete)
    else:
        print(comand-menu)

if __name__== "__main__":
    main()
