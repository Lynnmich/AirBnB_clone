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


    def do_create(self, args):
        """
        Create an instance of BaseModel
        Save it and prints its id.
        """
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True):
            return

        base_ = eval(nb_args[0])()
        base_.save()
        print(base_.id)

    def do_show(self, args):
        """
        Prints string representation of an Insatance
        """
        nb_args = args.split()
        if not self.check_if_args_is_correct(nb_args, True, True):
            return

        id = "{}.{}".format(nb_args[0], nb_args[1])
        print(str(models.storage.all()[id]))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
