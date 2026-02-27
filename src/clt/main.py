import cryptography
import argparse
import os

#Declaration of global variables and constants
security = "locked"
password = ""
command-menu = "" #Type in list of commands.



#Function Definitions
#Define a function to create a file if it doesn't exist. Or open it, if it does.
def create_file():

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
    os.makedirs(r"~\NOTEBOOK, mode=0o777, exist_ok=True") #most likely wrong usage
    #Parses user inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("--new", metavar="FILE", help="Creates a new encrypted file.")
    group.add_argument("--open", metavar="FILE", help="Decrypts and opens file.")
    group.add_argument("--login", metaver="USER", help="Authenticates user.")
    group.add_argument("--setup", action="store_true", help="Sets up new password")
    group.add_argument("--delete", metaver="FILE", help="Deletes specified file.")

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
