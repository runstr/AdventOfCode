import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    numbers = list(map(int,load_data_as_lines(filepath, example=EXAMPLE)))
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == 2020:
                return numbers[i]*numbers[j]

def smarter_solution():
    numbers = list(map(int, load_data_as_lines(filepath, example=EXAMPLE)))
    set_numbers = set(numbers)
    for i in range(len(numbers)):
        rest = 2020-numbers[i]
        if rest in set_numbers:
            return numbers[i]*rest


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = smarter_solution()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
