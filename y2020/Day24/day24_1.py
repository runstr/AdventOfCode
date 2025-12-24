import pathlib
import re

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

directions = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, -1),
    "nw": (0, -1),
    "se": (0, 1),
    "sw": (-1, 1)}


def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    visted = set()
    for line in data:
        current = (0, 0)
        for dir in re.findall("e|w|ne|nw|se|sw", line):
            current = (current[0]+directions[dir][0], current[1]+directions[dir][1])
        if current in visted:
            visted.remove(current)
        else:
            visted.add(current)

    return len(visted)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
