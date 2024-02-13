#!/usr/bin/python3

"""Command line console for the AirBnb clone"""

import cmd
import json
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt: str = '(hbnb) '
    fetched_objects = storage.all()
    all_classnames = []
    all_ids = []
    for key in fetched_objects.keys():
        classname, class_id = key.split('.')
        all_classnames.append(classname)


    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """An empty line should not execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg not in self.all_classnames:
                print("** class doesn't exist **")
            else:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)

    def do_show(self, arg):
        """
        prints the string representation of an instance
        based on the class name and id
        """
        self.fetched_objects = storage.all()
        arg_len = len(arg.split())
        if arg_len < 1:
            print("** class name missing **")
        elif arg_len < 2:
            if arg not in self.all_classnames:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            arg_classname, arg_id = arg.split(" ")
            key = f"{arg_classname}.{arg_id}"
            if key not in self.fetched_objects:
                print("** no instance found **")
            else:
                print(self.fetched_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance and saves the changes  into the JSON file"""
        arg_len = len(arg.split())
        if arg_len < 1:
            print("** class name missing **")
        elif arg_len < 2:
            if arg not in self.all_classnames:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            arg_classname, arg_id = arg.split(" ")
            key = f"{arg_classname}.{arg_id}"
            if key in self.fetched_objects:
                del self.fetched_objects[key]
                FileStorage().save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """prints string representation of all instances"""
        str_rpr = []
        if arg:
            if arg not in self.all_classnames:
                print("** class doesn't exist **")
            else:

                for value in self.fetched_objects.values():
                    if value.__class__.__name__ == "BaseModel":
                        str_rpr.append(str(value))
                print(str_rpr)
        else:
            for value in self.fetched_objects.values():
                str_rpr.append(str(value))
            print(str_rpr)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg_len = len(arg.split())
        if arg_len < 1:
            print("** class name missing **")
        elif arg_len < 2:
            if arg not in self.all_classnames:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif arg_len < 3:
            classname, class_id = arg.split(" ")
            key = f"{classname}.{class_id}"
            if key not in self.fetched_objects:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif arg_len < 4:
            print("** value missing **")
        else:
            classname, class_id, attr, val = arg.split()
            key = f"{classname}.{class_id}"
            to_update = self.fetched_objects.get(key)
            setattr(to_update, attr, val)
            to_update.save()
            print(to_update)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
