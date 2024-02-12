#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Command to exit the program"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line should not execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
