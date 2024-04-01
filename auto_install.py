# Name: auto_install.py
# author: AbianSL
# Date: 2024-04-01
# Version: 0.1
# Description: This script contain the main function

import argparse

def main():
    parser = argparse.ArgumentParser(description="Install packages, or update the packages")
    parser.add_argument("-e", "--edit", help="add, edit, or delete packages information or package manager", action="store_true")
    args = parser.parse_args()

    if args.edit:
        print("Edit packages information")
    else:
        print("Install packages")

if __name__ == "__main__":
    main()
