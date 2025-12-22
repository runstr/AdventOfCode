import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    list_of_numbers = list(map(int,load_data(filepath, example=EXAMPLE).split(",")))
    spoken = {}
    for i in range(len(list_of_numbers)-1):
        spoken[list_of_numbers[i]] = i
    last_spoken = list_of_numbers[-1]
    list_of_numbers = list_of_numbers[:-1]
    for i in range(len(list_of_numbers), 2020):
        if last_spoken not in spoken:
            next_spoken = 0
            spoken[last_spoken] = i
        else:
            next_spoken = i-spoken[last_spoken]
            spoken[last_spoken] = i
        if i ==2020 -1:
            break
        last_spoken = next_spoken

    return last_spoken


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
