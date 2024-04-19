# Name: interface.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-06
# Version: 0.1
# Description: contain a class to manage the interface 

import curses

class general_menu:
    def __init__(self, items: list) -> None:
        self.items = items
        self.selected = 0
    
    def display(self, stdscr) -> None:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        for idx, item in enumerate(self.items):
            x_coordinate = width//2 - len(item)//2
            y_coordinate = height//2 - len(self.items)//2 + idx

            if idx == self.selected:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y_coordinate, x_coordinate, item)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y_coordinate, x_coordinate, item)
        
        stdscr.refresh()
