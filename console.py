#!/usr/bin/python3

import cmd
import sys

"""console class"""

class HBNBCommand(cmd.Cmd):
    """Accepts commands via the normal prompt or on the commadline"""
    prompt = "(hbnb)"
    def do_EOF(self, args):
        """To exit the commandline. Usage: EOF"""
        return True
    def do_quit(self, args):
        """To exit the commandline. Usage: quit"""
        return True


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
