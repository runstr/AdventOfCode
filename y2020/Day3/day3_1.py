import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution, load_data_as_map
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False


def get_my_answer():
    data, max_x, max_y = load_data_as_map(filepath, example=EXAMPLE)
    x, y = 0, 0
    dx, dy = 3, 1
    trees = 0
    while y < max_y:
        if data[(x, y)] == "#":
            trees += 1
        x = (x+dx) % max_x
        y = y + dy
    return trees


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
