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

        letter_j = ord("j")
        letter_k = ord("k")
        letter_l = ord("l")
        letter_h = ord("h")

        while True:
            key = stdscr.getch()

            if (key == curses.KEY_UP or key == letter_k)  and self.selected > 0:
                self.selected -= 1
            elif (key == curses.KEY_DOWN or key == letter_j) and self.selected < len(self.items) - 1:
                self.selected += 1
            elif key == curses.KEY_ENTER in [10, 13]:
                stdscr.clear()
                stdscr.addstr(height//2, width//2 - 4, f"Selected {self.items[self.selected]}")
                stdscr.refresh()
                stdscr.getch()
                break

            stdscr.clear()
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
        # to see the result
        stdscr.getch()
    def close(self, stdscr) -> None:
        curses.endwin()

curses.wrapper(general_menu(["Option 1", "Option 2", "Option 3"]).display)