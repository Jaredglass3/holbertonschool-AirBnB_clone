#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """main loop for commands"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """exits loop for quit"""
        raise SystemExit

    def do_EOF(self, args):
        """exits loop for EOF"""
        raise SystemExit

    def emptyline(self):
        """nothing for no input"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
