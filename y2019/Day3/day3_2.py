import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    top, bottom = load_data_as_lines(filepath, example=EXAMPLE)
    top, bottom = top.split(","), bottom.split(",")
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0,-1)}
    point = (0,0)
    all_moves = {}
    total_steps = 0
    # First find all moves
    for move in top:
        dir, steps = move[0], int(move[1:])
        for i in range(steps):
            next_point = (point[0]+directions[dir][0], point[1]+directions[dir][1])
            point = next_point
            total_steps+=1
            all_moves[point] = total_steps
    point = (0,0)
    total_steps=0
    minimum = math.inf
    for move in bottom:
        dir, steps = move[0], int(move[1:])
        for i in range(steps):
            next_point = (point[0]+directions[dir][0], point[1]+directions[dir][1])
            point = next_point
            total_steps+=1
            if point in all_moves:
                if all_moves[point]+total_steps<minimum:
                     minimum=all_moves[point] + total_steps
    return minimum


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
