#!/usr/bin/python3
"""
This contains th Entry point of the command interpreter
"""
import cmd
import sys

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
