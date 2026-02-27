import cryptography
import argparse


# Once class per custom Action for text parsing.
class NewFileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

class OpenFileAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

class PasswordAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

class DeleteAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):

def main():
    #Parses inputs into executable commands for the program.
    parser = argparse.ArgumentParser(prog="NOTES")

    parse.add_argument("--quit", action="store_true")
    parse.add_argument("--new", action=NewFileAction, help="Creates a new encrypted file.")
    parse.add_argument("--open", action=OpenFileAction, help="Decrypts and opens file.")
    parse.add_argument("--login", action=PasswordAction, help="Authenticates user.")
    parse.add_argument("--delete", action=DeleteAction, help="Deletes specified file.")
    parse.add_argument("--help", action="help")

    args = parser.parse_args()

    state = standby

    while state = standby:
    




if __name__== "__main__":
    main()
