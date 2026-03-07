import argparse
import base64
from os import urandom
import cryptography
from pathlib import Path

#Declaration of global variables and constants
command-menu = "" #Type in list of commands.
salt = urandom(16)
folder = Path("NOTEBOOK")

#Function Definitions
#Define a function to create a file if it doesn't exist. Or open it, if it does.
def open_file():
    try:
        with open(f"NOTEBOOK/{file_name}.txt", "r") as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("File does not exits O_O")

#Define a function to setup a password.
def set_up():
    global password

    r_password = ""

    print("Input Password: ")
    password = input()

    print("Confirm Password.")
    r_password = input()

    if password == r_password:
        pass
    else:
        print("Passwords do not match. Try again.")

def derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            lengh = 32,
            salt = salt,
            iterations = 100_100,
            backen d= default_backend()
            )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))


#Define a function that can add a string to a file.
def write2():
    try:
        with open(f"folder/{file_name}.txt", "rw") as f:
            contents = f.read()
            print(contents)
            print(r"Add something. (If you want a new line, append \n at the end)")
            add_this = input()
            f.write(add_this)
        except FileNotFoundError:
            print("File doesn't exist???")

#Define a function to delete a specific file.
def delete():
    delete_this_file = Path(folder/{args.delete})
    try:
        os.remove(delete_this_file)
    except FileNotFoundError:
        print("File does not exist O_O")

#Define a function to encrypt a specific file.
def encrypt():
    data = ""
    with open(f"folder/{file_name}.txt", "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)

#Define a function to decrypt a specific file.
def decrypt():
    with open(file, "rb") as f:
        encrypted = f.read()

    
    decrypted = fernet.decrypt(encrypted)

    key = derive_key(password, salt)


    print(decrypted.decode(), end="")



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
        file_name = args.new
        open_file(file_name)
        encrypt(args.new)
    elif args.write:
        file_name = args.write
        write2(file_name)
    elif args.open:
        file_name = args.open
        decrypt(file_name)
        open_file(file_name)
    elif args.delete:
        delete_file(args.delete)
    else:
        print(comand-menu)

if __name__== "__main__":
    main()
