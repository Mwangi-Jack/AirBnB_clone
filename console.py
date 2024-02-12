#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt: str = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """An empty line should not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
