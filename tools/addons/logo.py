"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """"\033[5m"
               ▒▒████████      ▒▒█████████      ▒▒████████
              ▒▒██     ▒▒█      ▒▒██   ▒▒██      ▒▒██  ▒▒██
             ▒▒██               ▒▒██   ▒▒██      ▒▒██  ▒▒██
             ▒▒██               ▒▒██▒█████       ▒▒████████
              ▒▒██     ▒▒█      ▒▒██             ▒▒██  ▒▒██
               ▒▒████████      ▒▒███            ▒▒███  ▒▒██  V.02
           
           --------------- CYBER PEOPLE ATTACK ---------------
 
 ====================================|
 Mod --->>>> Abdullah Al Asad        |
 just for CPA members.               |
 This tool can detect existing sites |
 ====================================|
 """

    print(f"{F.GREEN}{logo}")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├───├ LAYER 7: ")
    print("    ├───>>>> - HTTP -")
    print("    ├───>>>> - HTTP-PROXY -")
    print("    ├───>>>> - SLOWLORIS -")
    print("    ├───>>>> - SLOWLORIS-PROXY -")
    print("    ├")

  
