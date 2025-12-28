import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = True

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    layers = []
    if EXAMPLE:
        width = 3
        height = 2
    else:
        width = 25
        height = 6
    for i in range(0, len(data), width*height):
        layers.append(data[i:i+width*height])

    min_layer = min(layers, key=lambda x: x.count("0"))
    return min_layer.count("1")*min_layer.count("2")


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
