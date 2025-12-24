import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def build_map(data):
    full_circle = {}
    for i in range(0,len(data)-1):
        full_circle[data[i]] = data[i+1]
    full_circle[data[-1]] = 10
    for i in range(10, 1_000_000):
        full_circle[i] = i+1
    full_circle[1_000_000] = data[0]

    return full_circle


def get_my_answer():
    data = list(map(int,list(load_data(filepath, example=EXAMPLE))))
    full_circle = build_map(data)
    start_point = data[0]
    for i in range(1, 10_000_001):
        pick1 = full_circle[start_point]
        pick2 = full_circle[pick1]
        pick3 = full_circle[pick2]
        destination = start_point - 1
        if destination == 0:
            destination = 1_000_000
        test = []
        while destination == pick1 or destination == pick2 or destination == pick3:
            destination -= 1
            if destination == 0:
                destination = 1_000_000
        full_circle[start_point] = full_circle[pick3]
        full_circle[pick3] = full_circle[destination]
        full_circle[destination] = pick1

        # move current cup
        start_point = full_circle[start_point]
    first = full_circle[1]
    second = full_circle[first]
    return first*second

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
