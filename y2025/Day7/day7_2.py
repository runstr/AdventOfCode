import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
from functools import lru_cache


EXAMPLE = False
SUBMIT_ANSWER = False

tachyon_map={}
memory = {}


def upadate_map(string_map, new_index):
    string_map[new_index[1]] = string_map[new_index[1]][:new_index[0]]+"|"+string_map[new_index[1]][new_index[0]+1:]
    return string_map


def depth_search(next_point, max_y):
    while True:
        if next_point[1] == max_y:
            memory[next_point] = 1
            return 1
        if tachyon_map[next_point] == ",":
            next_point = (next_point[0], next_point[1]+1)
            continue
        else:
            break
    if next_point in memory:
        return memory[next_point]
    total = 0
    for point in [(next_point[0]+1, next_point[1]), (next_point[0]-1, next_point[1])]:
        total += depth_search(point, max_y)
    memory[next_point] = total
    return total

def while_loop(start, max_y):
    visited = set()
    next_visits = [start]
    total = 0
    while next_visits:
        next_visit = next_visits.pop()
        while tachyon_map[next_visit] == ",":
            next_visit = (next_visit[0], next_visit[1] + 1)
            if next_visit[1] == max_y:
                total += 1
                memory[next_visit] += 1
        if next_visit in visited:
            continue
        if next_visit in memory:
            total += memory[next_visit]
            continue
        for point in [(next_visit[0] + 1, next_visit[1]), (next_visit[0] - 1, next_visit[1])]:
            next_visits.append(point)
    return total

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    start = (-1, -1)
    max_x = len(data[1])
    max_y = len(data)
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == "S":
                start = (x, y)
                tachyon_map[(x, y)] = data[y][x]
            elif data[y][x] == ".":
                tachyon_map[(x, y)] = ","
            else:
                tachyon_map[(x, y)] = data[y][x]
    total = depth_search(start, max_y)

    return total


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
