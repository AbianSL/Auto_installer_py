# name: error.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-06
# Version: 0.1
# Description: This script contain the error class to manage the exceptions

class general_error:
    def __init__(self, error_name: Str, error_code = 0: int, error_msg = "": Str) -> None:
        self.error_name = 
        self.error_code = error_code

    def print_msg(self):
        print(f"Error {self._code}: {self._message}")
