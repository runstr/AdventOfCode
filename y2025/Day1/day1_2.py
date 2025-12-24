import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()


def get_my_answer():
    line_data = load_data_as_lines(filepath, example=False)
    dial = 50
    zero_times = 0
    for line in line_data:
        letter = line[0]
        number = int(line[1:])
        zero_times += number//100
        og_number = number
        number = number % 100
        if letter == "R":
            dial += number
            if dial >= 100:
                zero_times += 1
            dial = dial % 100
        else:
            if dial ==0:
                zero_times-=1
            dial -= number
            if dial <= 0:
                zero_times += 1
            dial = dial % 100
    return zero_times


@timeexecution
def execution():
    SUBMIT_ANSWER = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
