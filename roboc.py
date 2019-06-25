#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## maze
## File description:
## main function
##

import sys
sys.path.append('src/')
from open_file import *
from display import *
from moves import *

#I created my standard coding style so I don't put comment
#I have less than 5 functions
#I have less than 20 lines per functions
#I have less than 80 characters per lines
#Functions / Variables names need to be full explicit

class my_maze():
    def __init__(self):
        self.path = choose_directory()
        self.file_name = display_start(self.path)
        self.my_map = open_map(self.file_name, self.path)

    def __repr__(self):
        maze = "\n"
        for elem in self.my_map:
            maze += "".join(elem)
            maze += "\n"
        return (maze)

    def __str__(self):
        return (repr(self))

def save_map(maze, string):
    if (string == "q"):
        map = open(maze.path + "/" + maze.file_name.split(".txt")[0] +
                   "_save.txt", "w")
        my_maze = ""
        for elem in maze.my_map:
            my_maze += "".join(elem)
            my_maze += "\n"
        map.write(my_maze)
        map.close()
        print("The map has been successfully saved")
        print("Name : " + maze.path + "/" + maze.file_name.split(".txt")[0] +
              "_save.txt")
        exit(0)

def maze():
    maze = my_maze()
    print(maze)
    before = " "
    pos_player = get_pos_player(maze.my_map)
    while (1):
        choice = pars()
        save_map(maze, choice)
        before = moove(choice, maze.my_map, before, pos_player)
        print(maze)
        if (before == "U"):
            print("Congratulation ! You won !")
            exit(0)
        pos_player = get_pos_player(maze.my_map)

maze()
