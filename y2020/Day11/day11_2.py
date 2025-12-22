import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, load_data_as_map, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
def check_directions(x,y, dx, dy, full_map):
    i = 1
    while True:
        new_pos = (x + dx*i, y + dy*i)
        if new_pos in full_map:
            if full_map[new_pos] != ".":
                return full_map[new_pos]
            else:
                i+=1
                continue
        break
    return "."


def get_my_answer():
    full_map, max_x, max_y = load_data_as_map(filepath, example=EXAMPLE)
    changes = 1
    while changes:
        changes = []
        for y in range(max_y):
            for x in range(max_x):
                letters = ""
                this_seat = full_map[(x, y)]
                if this_seat == ".":
                    continue
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    letters+=check_directions(x,y, dx, dy, full_map)
                if this_seat == "#" and letters.count("#") >= 5:
                    changes.append(((x, y), "L"))
                elif this_seat == "L" and "#" not in letters:
                    changes.append(((x, y), "#"))
        for change in changes:
            full_map[change[0]] = change[1]
    return list(full_map.values()).count("#")


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
