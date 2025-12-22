import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    start_time, busses = data.split("\n")
    start_time = int(start_time)
    busses = busses.split(",")
    busses = list(map(int, [a for a in busses if a != "x"]))
    differences = []
    for a in busses:
        diff = int(start_time/a+1)*a-start_time
        differences.append((diff,a))
    minimum = min(differences, key=lambda x: x[0])
    return minimum[1]*minimum[0]


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
