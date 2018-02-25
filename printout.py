# -*- coding: utf-8 -*-
import platform

class color:
    color_code = {
        'black' : 30, 'red' : 31, 'green' : 32,
        'yellow' : 33, 'blue' : 34, 'magenta' : 35,
        'cyan' : 36 }
    special_code = { 'end' : 0}

    def end(self):
        if platform.system() == 'Windows':
            return ""
        return "\033[{}m".format(self.special_code['end'])

    def set(self, color_fg, light=True, color_bg = None):
        if platform.system() == 'Windows':
            return ""
        fg = self.color_code[color_fg]
        if light:
            fg += 60
        return "\033[{}m".format(fg)

def print_warning(string, endl=True):
    print_color(string, "yellow", endl=endl, light=True)

def print_error(string, endl=True):
    print_color(string, "red", endl=endl, light=True)

def print_blue(string, endl=True, light=True):
    print_color(string, "blue", endl=endl, light=light)

def print_cyan(string, endl=True, light=True):
    print_color(string, "cyan", endl=endl, light=light)

def print_magenta(string, endl=True, light=True):
    print_color(string, "magenta", endl=endl, light=light)

def print_color(string, color_string, endl=True, light=True):
    c = color()
    s = "{}{}{}".format(c.set(color_string, light=light), string, c.end())
    if endl:
        print(s)
    else:
        print_no_line(s)

def print_no_line(string):
    print(string, end='')

def test():
    print_warning("This is a warning!")
    print_error("This is an error!")
    print_blue("This is a print_blue!")
    print_cyan("This is a print_cyan!")
    print_magenta("This is a print_magenta!")
