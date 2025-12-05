import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    ranges, ingredients = data.split("\n\n")
    ranges = ranges.split("\n")
    list_ranges = []
    for subrange in ranges:
        start, end = subrange.split("-")
        list_ranges.append((int(start), int(end)))
    fresh = 0
    for ingredient in ingredients.split("\n"):
        for r in list_ranges:
            if r[0] <=int(ingredient)<=r[1]:
                fresh+=1
                break
    return fresh


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
