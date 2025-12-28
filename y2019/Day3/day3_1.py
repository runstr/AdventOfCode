import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

from y2020.Day24.day24_1 import directions

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    top, bottom = load_data_as_lines(filepath, example=EXAMPLE)
    top, bottom = top.split(","), bottom.split(",")
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0,-1)}
    point = (0,0)
    points_top = set()
    for move in top:
        dir, steps = move[0], int(move[1:])
        for i in range(steps):
            next_point = (point[0]+directions[dir][0], point[1]+directions[dir][1])
            points_top.add(next_point)
            point = next_point
    point = (0,0)
    minimum = math.inf
    for move in bottom:
        dir, steps = move[0], int(move[1:])
        for i in range(steps):
            next_point = (point[0]+directions[dir][0], point[1]+directions[dir][1])
            point = next_point
            if point in points_top:
                if abs(point[0])+abs(point[1])<minimum:
                     minimum=abs(point[0])+abs(point[1])
    return minimum


def get_my_answer_faster():
    top, bottom = load_data_as_lines(filepath, example=EXAMPLE)
    top, bottom = top.split(","), bottom.split(",")
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0,-1)}
    point = (0, 0)
    vertical_segments = {}
    horizontal_segments = {}
    for move in top:
        dir, steps = move[0], int(move[1:])
        next_point = (point[0]+directions[dir][0]*steps, point[1]+directions[dir][1]*steps)
        if dir == "R" or dir == "L":
            horizontal_segments[point[1]]=(point[0], next_point[0])
        else:
            vertical_segments[point[0]]=(point[1], next_point[1])
        point = next_point
    point=(0,0)
    minimum = math.inf
    for move in bottom:
        dir, steps = move[0], int(move[1:])
        next_point = (point[0]+directions[dir][0]*steps, point[1]+directions[dir][1]*steps)
        if dir == "R" or dir == "L":
            for x, ys in vertical_segments.items():
               if (min(point[0], next_point[0])<= x <= max(point[0], next_point[0]) and
                       min(ys[0], ys[1])<= point[1] <= max(ys[0], ys[1])):
                   dist = abs(x)+abs(point[1])
                   if dist < minimum:
                       minimum = dist

        else:
            for y, xs in horizontal_segments.items():
               if (min(point[1], next_point[1])<= y <= max(point[1], next_point[1]) and
                       min(xs[0], xs[1])<= point[0] <= max(xs[0], xs[1])):
                   dist = abs(y)+abs(point[0])
                   if dist < minimum:
                       minimum = dist
        point = next_point
    return minimum

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer_faster()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
