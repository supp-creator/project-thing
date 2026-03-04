import argparse
import base64
import os
import cryptography

#Declaration of global variables and constants
security = "locked"
password = ""
command-menu = "" #Type in list of commands.
file = ""
salt =



#Function Definitions
#Define a function to create a file if it doesn't exist. Or open it, if it does.
def create_file():
    with open("NOTEBOOK/{}.txt".format(args.new), "w")

    salt = os.random(16)

#Define a function to open a specific file.
def open_file():

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

#Define a function to authenticate a password.
def login():
    global security


#Define a function to delete a specific file.
def delete():

#Define a function to encrypt a specific file.
def encrypt():
    with open(file, "rb") as f:
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
    os.makedirs("~\NOTEBOOK, mode=0o777, exist_ok=True") 

    #Parses user inputs into executable commands for the program.

    parser = argparse.ArgumentParser(prog="NOTES")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--new")
    group.add_argument("--open")
    group.add_argument("--login")
    group.add_argument("--setup")
    group.add_argument("--delete")

    args = parser.parse_args()

    #Decision Tree
    if args.new:
        create_file(args.new)
        encrypt(args.new)
    elif args.login:
        login(args.login)
    elif args.open:
        if security == "locked":
            print("Please login to decrypt file.")
        else:
            decrypt(args.open)
            open_file(args.open)
    elif args.delete:
        delete_file(args.delete)
    else:
        print(comand-menu)

if __name__== "__main__":
    main()
