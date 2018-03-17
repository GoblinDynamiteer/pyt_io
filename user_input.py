# -*- coding: utf-8 -*-

import sys, printout

def yes_no(question, default="yes", script_name=None):
    valid = {"yes": True, "y": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        print("yes_no: wrong default.")
        quit()

    while True:
        if script_name:
            printout.print_script_name(script_name, "", endl=False)
        sys.stdout.write("{} {}".format(question, prompt))
        choice = input().lower()
        if default is not None and choice is '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Enter Yes/No!")
