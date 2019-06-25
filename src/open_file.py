#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## maze
## File description:
## open_file
##

import os
import pickle

class Error(Exception):
    pass

class EmptyFolder(Error):
    pass

class OutLimit(Error):
    pass

def open_map(map_file, path):
    try:
        with open(path + "/" + map_file, "r") as my_file:
            my_map = str(my_file.read()).split("\n")
            new_map = []
            for enum, val in enumerate (my_map):
                if (list(val) != []):
                    new_map.append(list(val))
        return (new_map)
    except FileNotFoundError:
        print("Error:File not found")
        exit(84)

def check_inside_file(my_list, path):
    for string in my_list:
        with open(path + "/" + string, "r") as my_file:
            map_read = my_file.read()
            letter_x = 0
            letter_u = 0
        for letter in map_read:
            if (letter != 'O' and letter != 'U' and letter != '.' and
                letter != 'X' and letter != ' ' and letter != '\n'):
                my_list.remove(string)
            if (letter == 'X'):
                letter_x += 1
            if (letter == 'U'):
                letter_u += 1
        if (letter_x > 1 or letter_u == 0):
            my_list.remove(string)

def check_inside_list(my_list, path):
    new_list = []
    for string in my_list:
        correct = 0
        name = list(string)
        len_name = len(name)
        for enum, val in enumerate (name):
            if (val == '.' and len_name - enum == 4 and name[enum + 1] == 't'
                and name[enum + 3] == 't' and name[enum + 2] == 'x'):
                correct = 1
        if (correct == 1):
            if (os.path.isfile(path + "/" + string) == True):
                new_list.append(string)
    return (new_list)

def open_folder(path):
    maps_name = []
    try:
        maps_name = os.listdir(path)
        if (maps_name == []):
            raise EmptyFolder
        maps_name = check_inside_list(maps_name, path)
        check_inside_file(maps_name, path)
    except FileNotFoundError:
        print("Error:Folder '{}' not found.".format(path))
        return ([])
    except EmptyFolder:
        print("Error:No map found in '{}.'".format(path))
        return ([])
    return (maps_name)
