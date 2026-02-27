import cryptography
import argparse
import os

#Declaration of global variables and constants

security = "locked"
password = ""


#Function Definitions
#Define a function to create a file if it doesn't exist. Or open it, if it does.
def create_file():

#Define a function to open a specific file.
def open_file():

#Define a function to setup a password.
def set_up():
    global password


#Define a function to authenticate a password.
def password():
    global security


#Define a function to delete a specific file.
def delete():

#Define a function to encrypt a specific file.
def encrypt():

#Define a function to decrypt a specific file.
def decrypt():



def main():
    # Creates a folder to store all files, makes one if it doesn't exit yet.
    os.makedirs("NOTEBOOK", exist_ok=True)
    #Parses user inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES")

    parser.add_argument("--quit", action="store_true")
    parser.add_argument("--new", help="Creates a new encrypted file.")
    parser.add_argument("--open", help="Decrypts and opens file.")
    parser.add_argument("--login", help="Authenticates user.")
    parser.add_argument("--setup", help="Sets up new password (Can only be done once.)")
    parser.add_argument("--delete", help="Deletes specified file.")
    parser.add_argument("--help", action="help")

    args = parser.parse_args()

    #Decision Tree
    if args.new:
        create_file(args.new)
        encrypt(args.new)
    elif args.login:
        login(args.login)
    elif args.open:
        if security == "locked":
            print("Please login before to decrypt file.")
        else:
            decrypt(args.open)
            open_file(args.open)
    elif args.delete:
        delete_file(args.delete)

if __name__== "__main__":
    main()
