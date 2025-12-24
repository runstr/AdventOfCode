import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
import re

directions = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, -1),
    "nw": (0, -1),
    "se": (0, 1),
    "sw": (-1, 1)}

def get_adjacent_tiles(black_tiles):
    white_tiles = set()
    for black_tile in black_tiles:
        for dir in directions.values():
            white_tile = (black_tile[0] + dir[0], black_tile[1] + dir[1])
            if white_tile not in black_tiles:
                white_tiles.add(white_tile)
    return white_tiles


def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    black_tiles = set()
    for line in data:
        current = (0, 0)
        for dir in re.findall("e|w|ne|nw|se|sw", line):
            current = (current[0]+directions[dir][0], current[1]+directions[dir][1])
        if current in black_tiles:
            black_tiles.remove(current)
        else:
            black_tiles.add(current)
    for i in range(0, 100):
        white_tiles = get_adjacent_tiles(black_tiles)
        new_black_tiles = set()
        for white_tile in white_tiles:
            adjacent_tiles = 0
            for dir in directions.values():
                adjacent_tile = (white_tile[0] + dir[0], white_tile[1] + dir[1])
                if adjacent_tile in black_tiles:
                    adjacent_tiles += 1
            if adjacent_tiles == 2:
                new_black_tiles.add(white_tile)
        for black_tile in black_tiles:
            adjacent_tiles = 0
            for dir in directions.values():
                adjacent_tile = (black_tile[0] + dir[0], black_tile[1] + dir[1])
                if adjacent_tile in black_tiles:
                    adjacent_tiles += 1
            if adjacent_tiles == 1 or adjacent_tiles == 2:
                new_black_tiles.add(black_tile)
        black_tiles=new_black_tiles
    return len(new_black_tiles)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
