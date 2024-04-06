# name: error.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-06
# Version: 0.1
# Description: This script contain the error class to manage the exceptions

class error_mg:
    def __init__(self, error_file: str, code: int):
        with open(error_file, "r") as file:
            self._message = file.read()
        self._code = code

    def print_msg(self):
        print(f"Error {self._code}: {self._message}")
