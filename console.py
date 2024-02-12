#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Prints help for the quit command"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """An empty line should not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
