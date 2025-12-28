import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    old_data = list(map(int,load_data(filepath, example=EXAMPLE).split(",")))
    final = 19690720
    for noun in  range(0,99):
        for verb in range(0,99):
            data = old_data[:]
            data[1] = noun
            data[2] = verb
            for i in range(0, len(data), 4):
                if data[i] == 1:
                    data[data[i+3]] = data[data[i+2]] + data[data[i+1]]
                elif data[i] == 2:
                    data[data[i+3]] = data[data[i+2]] * data[data[i+1]]
                elif data[i] == 99:
                    break
            if data[0]==final:
                return 100 * noun + verb




@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
