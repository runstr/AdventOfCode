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
    full_circle[data[-1]] = data[0]
    return full_circle


def get_my_answer():
    data = list(map(int,list(load_data(filepath, example=EXAMPLE))))
    full_circle = build_map(data)
    start_point = data[0]
    print_map(full_circle, 0, 3)
    for i in range(1, 101):
        next_points = []
        pick = start_point
        for _ in range(0,3):
            pick = full_circle[pick]
            next_points.append(pick)
        destination = start_point - 1
        if destination == 0:
            destination = 9
        while destination in next_points:
            destination -= 1
            if destination == 0:
                destination = 9
        full_circle[start_point] = full_circle[next_points[2]]
        full_circle[next_points[2]] = full_circle[destination]
        full_circle[destination] = next_points[0]

        # move current cup
        start_point = full_circle[start_point]
    #print(i)
    final_map = print_map(full_circle, 0, 1)
    return final_map[1:]

def print_map(full_circle, index, start_point):
    string = ["0"]*9
    next_point = start_point
    for i in range(9):
        string[(index+i)%9] = str(next_point)
        next_point = full_circle[next_point]
    return "".join(string)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
