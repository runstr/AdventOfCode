import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def check_validity(this_number, previous_number):
    for i in range(len(previous_number)-1):
        for j in range(i, len(previous_number)):
            if previous_number[i] + previous_number[j] == this_number:
                return True
    return False


def get_my_answer():
    numbers = list(map(int,load_data_as_lines(filepath, example=EXAMPLE)))
    preamble = 5
    for i in range(preamble, len(numbers)):
        previous_numbers = numbers[i-preamble:i]
        if not check_validity(numbers[i], previous_numbers):
            break

    return numbers[i]


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
