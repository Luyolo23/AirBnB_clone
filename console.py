#!/usr/bin/python3
"""The Console Module"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    MODEL_CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def empty_line(self):
        """Handles empty lines gracefully.
        This method is called when an empty line is entered.
        It does nothing, allowing the user to enter a new command.
        """
        pass

    def do_EOF(self, line):
        """Exits the console on EOF (Ctrl+D) command.
        Triggered when the user presses Ctrl+D. It prints a newline character
        and returns True to exit the command loop.
        """
        print()
        return True

    def help_quit(self):
        """Provides help for the 'quit' command.
        This method prints a help message for the 'quit' command,
        explaining how to use it to exit the program.
        """
        print("Quit command to exit the program\n")

    def do_quit(self, line):
        """Quits the program.
        This method is triggered by the 'quit' command. It returns True
        to exit the command loop and terminate the program.
        """
        return True

    def processes_custom_command(self, class_name, action):
        """Processes custom commands for model instances.
        This method handles custom commands that operate on model instances,
        such as 'show', 'all', 'count', 'destroy', and 'update'.
        Parameters:
        - class_name (str): The name of the model class.
        - action (str): The action to perform, including any arguments.
        Returns:
        - None
        """
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(')'):
            action_name = parts[0]
            action_args = parts[1][:-1].split(',')

            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif action_name == 'destroy':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            elif action_name == 'update':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]

                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handles unrecognized commands.
        This method is called when an unrecognized command is entered.
        It attempts to process the command as a custom command.
        Parameters:
        - line (str): The command line entered by the user.
        Returns: None
        """
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.processes_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")

    def do_create(self, linE):
        """Creates a new instance of a specified model class.
        This method creates a new instance of the specified model
        class and saves it to the JSON file.
        Parameters:
        - line (str): The command line entered by the user,
        including the class name.
        Returns: None
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.MODEL_CLASSES:
            print("** class doesn't exist **")
            return

        try:
            instance = self.MODEL_CLASSES[class_name]()
            instance.save()
            print(instance.id)
        except TypeError as e:
            print(f"** Error creating instance: {e} **")
        except Exception as e:
            print(f"** Error saving instance: {e} **")



    def do_show(self, line):
        """Displays the string representation of a specified model instance.
        This method prints the string representation of the specified model
        instance based on the class name and id.
        Parameters:
        - line (str): The command line entered by the user,
        including the class name and id.
        Returns: None
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.MODEL_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes a specified model instance
        then saves the change into the JSON file."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.MODEL_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Lists all instances of a specified model class.
        This method lists all instances of the specified model class,
        or all instances if no class is specified.
        Parameters:
        - line (str): The command line entered by the user,
        optionally including the class name.
        Returns: None
        """
        args = line.split()

        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.MODEL_CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        """Updates a specified model instance.
        This method updates a specified model instance by adding or
        updating an attribute, and saves the change to the JSON file.
        Parameters:
        - line (str): The command line entered by the user, including
        the class name, id, attribute name, and new value.
        Returns: None
        """
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.MODEL_CLASSES:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]

        setattr(obj, attribute, value)
        storage.all()[key].save()

    def cmdloop(self, intro=None):
        """Override cmdloop to handle KeyboardInterrupt.
        When user opts for 'ctrl+C' on keyboard instead of typing 'quit'
        """
        try:
            super().cmdloop(intro)
        except KeyboardInterrupt:
            print("\nExiting the program...")
            return False  # Return False to indicate the program should exit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
