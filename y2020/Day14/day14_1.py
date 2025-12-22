import pathlib
import re

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False


def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    memory = {}
    max_length = 36
    for line in data:
        a, b = line.split(" = ")
        if a == "mask":
            zeroes = [a.start() for a in re.finditer("0", b)]
            ones = [a.start() for a in re.finditer("1", b)]
            continue

        value = bin(int(b))[2:]
        value = list("0"*(36-len(value))+value)
        for zero in zeroes:
            value[zero] = "0"
        for one in ones:
            value[one] = "1"
        address = int(a[4:-1])
        memory[address] = int("".join(value),2)

    return sum(memory.values())


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
