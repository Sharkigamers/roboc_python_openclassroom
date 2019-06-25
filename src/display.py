#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## maze
## File description:
## diplay
##

from open_file import *

def choose_directory():
    try:
        path = str(input("Would you choose the directory of your mazes \
? (default:maps) [y/N] : ")).lower()
        if (path != "y" and path != "yes"):
            return ("maps")
        path = str(input("Select the repository containing your maps : "))
        return (path)
    except (KeyboardInterrupt, EOFError):
            exit(1)

def selection(enum):
    while (1):
        try:
            choice = int(input("\nEnter a number for starting a game : "))
            if (choice <= 0 or choice > (enum + 1) or type(choice) != int):
                raise OutLimit
            break
        except (ValueError, OutLimit):
            print("Select a number beetween [{}, {}].".format("1", enum + 1))
        except (KeyboardInterrupt, EOFError):
            exit(1)
    return (choice)

def display_start(path):
    my_files = open_folder(path)
    if (my_files == []):
        exit(84)
    print("Existing mazes :")
    for enum, val in enumerate (my_files):
        print(str(enum + 1) + " - " + val.split(".txt")[0] + ".")
    choice = selection(enum)
    print("\nYou have chose the '{}' \
maze.".format(my_files[choice - 1].split(".txt")[0]))
    return (my_files[choice - 1])
