"""
This program is mainly for checking if you have all the dependencies installed.
NOTE: This program is only to be run when you're developing the game and should not be included in the base game.
"""

import sys

issue_flag = False

# VE checks

# Idk how to pull this off...

# Module checks

def missing_module_message(display_name: str, pipi_name: str):
    print(f"{display_name} module is not installed into this environment. Please install the module using: `pip install {pipi_name}`")

try:
    import pygame
except ImportError:
    missing_module_message("Pygame-CE", "pygame-ce")
    issue_flag = True

if issue_flag:
    sys.exit("Cannot run game with these issues still persisting. Please fix the dependency issues before you run the game again.")

else:
    import main