#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## maze
## File description:
## moove
##

def get_pos_player(my_map):
    for enum, elem in enumerate (my_map):
        for count, chara in enumerate (my_map[enum]):
            if (chara == "X"):
                return ([enum, count])

def pars():
    success = 1
    while (success):
        try:
            choice = str(input("> ")).lower()
            success = 0
            if (len(choice) == 0):
                success = 1
            elif (len(choice) == 1 and choice != "n" and choice != "s" and
                  choice != "e" and choice != "o" and choice != "q"):
                success = 1
            elif (len(choice) != 1):
                for enum, letter in enumerate (choice):
                    if ((enum == 0 and letter != "n" and letter != "s" and
                        letter != "e" and letter != "o" and choice != "q")
                        or (enum > 0 and (letter < "0" or letter > "9"))):
                        success = 1
        except (KeyboardInterrupt, EOFError):
            exit(1)
    return (choice)

def multiple_moove(string, maze, before, pos):
    chara_moove = str(string[:1])
    nb_moove = int(string[1:])
    for i in range (nb_moove):
        before = moove(chara_moove, maze, before, pos)
        pos = get_pos_player(maze)
        if (before == "U"):
            break
    return (before)

def moove(string, maze, before, pos):
    if (len(string) == 1):
        maze[pos[0]][pos[1]] = before
        if (string == "n" and maze[pos[0] - 1][pos[1]] != "O"):
            before = maze[pos[0] - 1][pos[1]]
            maze[pos[0] - 1][pos[1]] = "X"
        elif (string == "s" and maze[pos[0] + 1][pos[1]] != "O"):
            before = maze[pos[0] + 1][pos[1]]
            maze[pos[0] + 1][pos[1]] = "X"
        elif (string == "e" and maze[pos[0]][pos[1] + 1] != "O"):
            before = maze[pos[0]][pos[1] + 1]
            maze[pos[0]][pos[1] + 1] = "X"
        elif (string == "o" and maze[pos[0]][pos[1] - 1] != "O"):
            before = maze[pos[0]][pos[1] - 1]
            maze[pos[0]][pos[1] - 1] = "X"
        else:
            maze[pos[0]][pos[1]] = "X"
    else:
        before = multiple_moove(string, maze, before, pos)
    return (before)
