import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_area(x1, y1, x2, y2):
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)
def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    maximum = 0
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            x1, y1 = map(int, data[i].split(","))
            x2, y2 = map(int, data[j].split(","))
            area = get_area(x1, y1, x2, y2)
            if area > maximum:
                maximum=area
    return maximum


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
