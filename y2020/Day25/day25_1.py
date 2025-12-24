import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    my_answer = list(map(int,load_data_as_lines(filepath, example=EXAMPLE)))
    div_value = 20201227
    subject_number = 7
    loop_count = 0
    value = 1
    retval = False
    while loop_count<1000000000:
        value *= subject_number
        value %= div_value
        loop_count += 1
        if value == my_answer[0]:
            retval = (loop_count, my_answer[1])
            break
        if value == my_answer[1]:
            retval = (loop_count, my_answer[0])

    value = 1
    for i in range(0,retval[0]):
        value *= retval[1]
        value %= div_value


    return value


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
