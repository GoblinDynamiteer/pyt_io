# -*- coding: utf-8 -*-
import sys, printout, os
from printout import print_class as pr

pr1 = pr(os.path.basename(__file__))

def yes_no(question, default="yes", script_name=None):
    valid = {"yes": True, "y": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        pr1.error("wrong default")
        quit()
    while True:
        if script_name:
            pr2 = pr(script_name)
        else:
            pr2 = pr(os.path.basename(__file__))
        pr2.info("{} {}".format(question, prompt), end_line=False)
        choice = input().lower()
        if default is not None and choice is '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            pr2.error("Enter Yes/No!")
