# Name: memory.py
# author: AbianSL (Abian Santana Ledesma)
# Date: 2024-04-06
# Version: 0.1
# Description: This script contain the memory class to manage the information
#               about the packages and the package manager

import error.error_mg as error

class memory:
    def __init__(self, packages_file: str, packages_managers: str):
        self._packages_file = package_file
        self._packages_managers = package_manager

        try:
            with open(self._packages_files, "r") as file:
                self._packages = file.readlines()
        except FileNotFoundError:
            error.error_mg("The file with the packages information does not exist")
            self._packages = []
            
            
