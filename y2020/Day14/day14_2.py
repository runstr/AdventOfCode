import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
import re

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    memory = {}
    max_length = 36
    for line in data:
        a, b = line.split(" = ")
        if a == "mask":
            xes = [a.start() for a in re.finditer("X", b)]
            ones = [a.start() for a in re.finditer("1", b)]
            continue
        address = int(a[4:-1])
        address = bin(int(address))[2:]
        address = list("0"*(max_length-len(address))+address)
        for one in ones:
            address[one] = "1"
        addresses = ["".join(address)]
        for index in xes:
            new_addresses = []
            for address in addresses:
                address = list(address)
                address[index] = "0"
                new_addresses.append("".join(address))
                address[index] = "1"
                new_addresses.append("".join(address))
            addresses = new_addresses
        for address in addresses:
            memory[int(address,2)] = int(b)
    return sum(memory.values())


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
