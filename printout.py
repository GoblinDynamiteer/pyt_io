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

def print_success(string, endl=True):
    print_color(string, "green", endl=endl, light=True)

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

def print_color_between(string, color_string, char_begin='[', char_end = ']', endl=True, light=True):
    c = color()
    start = string.find(char_begin) + 1
    end = string.find(char_end)

    color_string = "{}{}{}".format(c.set(color_string, light=light), string[start:end], c.end())
    print_no_line(string[0:start])
    print_no_line(color_string)

    if endl:
        print(string[end:])
    else:
        print_no_line(string[end:])

def print_no_line(string):
    print(string, end='')

def print_script_name(script_file_name, string, endl=True):
    end_line = False
    if endl:
        end_line = True
    print_color_between("[ {} ] {}".format(script_file_name, string), "green", endl=end_line)

def test():
    print_warning("This is a warning!")
    print_error("This is an error!")
    print_blue("This is a print_blue!")
    print_cyan("This is a print_cyan!")
    print_magenta("This is a print_magenta!")
    print_color_between("I want colors [BETWEEN] here", "red")
    print_color_between("I want colors ( BETWEEN * here", "yellow", char_begin='(', char_end='*')
