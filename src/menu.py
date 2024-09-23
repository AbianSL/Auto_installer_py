# Name: interface.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-06
# Version: 0.1
# Description: contain a class to manage the interface 

class general_menu:
    def __init__(self, items: list) -> None:
        self.items = items
        self.selected = 0
    
    def display(self, stdscr) -> None:
        stdscr.clear()
        for index, item in enumerate(self.items):
            if index == self.selected:
                stdscr.addstr(index, 0, f"> {item}")
            else:
                stdscr.addstr(index, 0, f"  {item}")
        stdscr.refresh()
