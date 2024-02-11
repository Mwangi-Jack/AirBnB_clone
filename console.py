#!/usr/bin/python3
import cmd
import sys
from unittest.mock import Base

from models import storage

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Accepts commands via the normal interactive
    prompt or on the command line.
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """creates a new instance of the BaseModel"""
        if not args:
            print("** class name missing **")
        if args != 'BaseModel':
            print("** class doesn't exist **")

        new_model = BaseModel()
        new_model.save()
        print(new_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based
        on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        all_objs = storage.all()
        obj_ids = []
        obj_names = []

        for key, value in all_objs.items():
            obj_name, obj_id = key.split(".")
            obj_ids.append(obj_id)
            obj_names.append(obj_name)

        args_len = len(args.split())

        if args_len < 1:
            print("** class name missing **")
        elif args_len == 1 and args not in obj_names:
            print("** class doesn't exist **")
        elif args_len < 2:
            print("** instance id missing **")
        else:
            class_name_inpt, class_id_inpt = args.split()
            if class_id_inpt not in obj_ids:
                print("** no instance found **")
            else:
                key = f"{class_name_inpt}.{class_id_inpt}"
                print(all_objs[key])

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits the commandline."""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # if len(sys.argv) > 1:
    #     HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    # else:
    #     HBNBCommand().cmdloop()
