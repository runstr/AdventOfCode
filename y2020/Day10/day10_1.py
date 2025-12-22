import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    joltages = list(map(int,(load_data_as_lines(filepath, example=EXAMPLE))))
    joltages.sort()
    joltages =[0] + joltages + [joltages[-1] + 3]
    single_volt = 0
    triple_volt = 0
    for i in range(0, len(joltages)-1):
        if joltages[i+1] - joltages[i] == 3:
            triple_volt += 1
        elif joltages[i+1] - joltages[i] == 1:
            single_volt += 1
    return single_volt*triple_volt


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
