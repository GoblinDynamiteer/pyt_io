# -*- coding: utf-8 -*-
import sys, printout
from printout import print_class as pr

def yes_no(question, default="yes", script_name=None):
    valid = {"yes": True, "y": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        pr.error("wrong default")
        quit()

    while True:
        if script_name:
            pr = pr(script_name)
        else:
            pr = pr(os.path.basename(__file__))
        pr.info("{} {}".format(question, prompt), end_line=False)
        choice = input().lower()
        if default is not None and choice is '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            pr.error("Enter Yes/No!")
