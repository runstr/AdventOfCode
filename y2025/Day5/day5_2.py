import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def check_if_in_range(number, rng):
    if rng[0]<=number<=rng[1]:
        return True
    else:
        return False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    ranges, ingredients = data.split("\n\n")
    ranges = ranges.split("\n")
    list_ranges = []
    for r in ranges:
        start, end = r.split("-")
        list_ranges.append((int(start), int(end)))
    list_ranges.sort()
    total_ranges = []
    for r in list_ranges:
        added = False
        new_total_ranges = []
        for tr in total_ranges:
            first = check_if_in_range(r[0], tr)
            second = check_if_in_range(r[1], tr)
            if first and second:
                new_total_ranges.append(tr)
                added = True
                break
            elif first and not second:
                new_range = (tr[0], r[1])
                new_total_ranges.append(new_range)
                added = True
                break
            else:
                new_total_ranges.append(tr)
                added = False
                continue
        if not added:
            new_total_ranges.append(r)
        total_ranges = new_total_ranges
    fresh = 0
    for i in total_ranges:
        fresh += (i[1]-i[0]+1)
    return fresh


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
