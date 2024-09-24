# Name: interface.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-19
# Version: 0.1
# Description: contain a class to manage the interface

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import menu

class main_interface(menu):
    def __init__(self, items: list) -> None:
        super().__init__(items)

    def display(self, stdscr) -> None:
        super().display(stdscr)
