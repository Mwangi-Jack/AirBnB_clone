#!/usr/bin/python3

"""Command line console for the AirBnb clone"""

import cmd
import json
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt: str = '(hbnb) '
    fetched_objects = storage.all()
    all_classnames = []
    all_ids = []
    for key, value in fetched_objects.items():
        classname, class_id = key.split('.')
        all_classnames.append(classname)
        all_ids.append(class_id)

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
                self.all_ids.append(new_model.id)
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
            if arg_id not in self.all_ids:
                print("** no instance found **")
            else:
                key = f"{arg_classname}.{arg_id}"
                print(self.fetched_objects.get(key))
                # print(f"{arg_classname} {arg_id}")

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
            if arg_id not in self.all_ids:
                print("** no instance found **")
            else:
                key = f"{arg_classname}.{arg_id}"
                del self.fetched_objects[key]
                for obj in self.fetched_objects.values():
                    new_model = obj
                    new_model.save()
                self.all_ids.remove(arg_id)
        self.fetched_objects = storage.all()

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
            if class_id not in self.all_ids:
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
