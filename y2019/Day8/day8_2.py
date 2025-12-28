import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    layers = []
    if EXAMPLE:
        width = 2
        height = 2
    else:
        width = 25
        height = 6

    for i in range(0, len(data), width*height):
        layers.append(data[i:i+width*height])
    final_layer = [["," for _ in range(width)] for _ in range(height)]
    for j in range(width*height):
        x=j%width
        y=j//width
        for layer in layers:
            color = layer[j]
            if color == "0":
                final_layer[y][x] = " "
                break
            elif color == "1":
                final_layer[y][x] = "o"
                break
    for layer in final_layer:
        print("".join(layer))
    #Answer: RCYKR
    return


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
