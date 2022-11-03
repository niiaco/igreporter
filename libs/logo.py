# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice
from pyfiglet import Figlet
from colored import attr,fg
#--------COLOR VARIABALES ------
reset = attr("reset")
red = fg("red")
green = fg("green")
yellow = fg("yellow")
white = fg("white")
magenta = fg("magenta")
light_red = fg("light_red")
cornsilk = fg("cornsilk_1")
gold = fg("gold_1")
orchid = fg("orchid_1")
bold = attr("bold")



def print_logo():
    custom_fig = Figlet(font='stop')
    print(gold + (custom_fig.renderText('IG reporter')) + reset + f"{bold}{cornsilk}IG REPORTER\n+ Developed By Niiaco{reset}")
