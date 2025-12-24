import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    # Follow formula for chineese remainder theorem
    data = load_data(filepath, example=EXAMPLE)
    busses = data.split("\n")[1].split(",")
    busses = [(int(busses[i]), i) for i in range(len(busses)) if busses[i] != "x"]
    new_busses = []
    for division, modulo in busses:
        if modulo>division:
            modulo = modulo%division
        new_busses.append((division, modulo))
    N = 1
    for bus in new_busses:
        N*=bus[0]
    N_i = []
    y_i = []
    for bus in new_busses:
        N_i.append(int(N/bus[0]))
        y_i.append(pow(int(N/bus[0]), -1, bus[0]))
    total_sum = 0
    for i in range(len(busses)):
        total_sum+=N_i[i]*y_i[i]*(-new_busses[i][1])
    return total_sum%N


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
