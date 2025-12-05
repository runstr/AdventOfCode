import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT = False


def get_my_answer():
    #data = load_data(filepath, example=EXAMPLE)
    line_data = load_data_as_lines(filepath, example=EXAMPLE)
    #int_data = load_data_as_int(filepath, example=EXAMPLE)
    dial = 50
    zero_times = 0
    for line in line_data:
        letter = line[0]
        number = int(line[1:])
        number = number%100

        if letter == "R":
            dial += number
            if dial >= 100:
                dial-= 100
        else:
            dial -= number
            if dial < 0:
                dial = 100+dial
        if dial == 0:
            zero_times+=1


    return zero_times


@timeexecution
def execution():
    submit_answer = SUBMIT
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
