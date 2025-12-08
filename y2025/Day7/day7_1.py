import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
import copy

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def upadate_map(string_map, new_index):
    string_map[new_index[1]] = string_map[new_index[1]][:new_index[0]]+"|"+string_map[new_index[1]][new_index[0]+1:]
    return string_map


def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    tachyon_map = {}
    start = (-1,-1)
    max_x = len(data[1])
    max_y = len(data)
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x]=="S":
                start=(x,y)
                tachyon_map[(x, y)] = data[y][x]
            elif data[y][x]==".":
                tachyon_map[(x, y)] = ","
            else:
                tachyon_map[(x, y)] = data[y][x]
    visited = set()
    next_visits = [start]
    splits = 0
    while next_visits:
        current = next_visits.pop()
        if current[1]+1 == max_y:
            continue
        next_visit = (current[0], current[1]+1)
        if next_visit in visited:
            continue
        if tachyon_map[next_visit] == ",":
            visited.add(next_visit)
            next_visits.append(next_visit)
            data = upadate_map(data, next_visit)
        else:
            splits+=1
            next_visit_neg = (current[0]-1, current[1]+1)
            if next_visit_neg not in visited:
                next_visits.append(next_visit_neg)
                data = upadate_map(data, next_visit_neg)
            next_visit_pos = (current[0]+1, current[1]+1)
            if next_visit_pos not in visited:
                next_visits.append(next_visit_pos)
                visited.add(next_visit_pos)
                data = upadate_map(data, next_visit_pos)

    return splits


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
