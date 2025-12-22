import pathlib
from math import ceil

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = True

def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    max_i_row = 6
    max_i_column = 9
    total = []
    for line in lines:
        lower, upper = 0, 127
        left, right = 0, 7
        row = -1
        column = -1
        for i, letter in enumerate(line):
            if letter == "F":
                upper = upper - ceil((upper-lower)/2)
            elif letter == "B":
                lower = lower + ceil((upper-lower)/2)
            elif letter == "L":
                right = right - ceil((right-left)/2)
            elif letter == "R":
                left = left + ceil((right-left)/2)
            if i==max_i_row:
                if letter == "B":
                    row = upper
                else:
                    row = lower
            elif i==max_i_column:
                if letter == "R":
                    column = right
                else:
                    column = left
        total.append(row*8+ column)
    total.sort()
    for i in range(total[0], total[-1]):
        if i not in total:
            return i
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
