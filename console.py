#!/usr/bin/python3
"""
This contains th Entry point of the command interpreter
"""
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter class
    """
    prompt = "(hnbn) "

    def do_quit(self, args):
        """
        Quit the promt
        """
        sys.exit(1)

    def do_EOF(self, args):
        """ Implement EOF so (Ctrl + D) will quit"""
        return True

    def emptyline(self):
        """
        If empty line
        """
        return

    def check_args(self, nb_args, check_clsname=True,
                                 check_id=False):
        """Check if passed args repect some
           Criteria
        """

        if (check_clsname):
            if not len(nb_args):
                print("** class name missing **")
                return 0

            try:
                base_ = eval(nb_args[0])()
                id = "{}.{}".format(nb_args[0], base_.id)
                del models.storage.all()[id]
                models.storage.save()
            except NameError:
                print("** class doesn't exist **")
                return 0

        if check_id:
            if len(nb_args) < 2:
                print("** instance id missing **")
                return 0

            id = "{}.{}".format(nb_args[0], nb_args[1])
            if (id not in models.storage.all().keys()):
                print("** no instance found **")
                return 0

        return 1 

if __name__ == "__main__":
    HBNBCommand().cmdloop()
