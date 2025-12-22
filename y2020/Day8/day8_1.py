import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def get_my_answer():
    instructions = load_data_as_lines(filepath, example=EXAMPLE)
    instruction = 0
    visited = set()
    acc=0
    while True:
        if instruction in visited:
            break
        visited.add(instruction)
        current = instructions[instruction]
        a, b = current.split(" ")
        if a =="jmp":
            instruction+= int(b)
            continue
        elif a == "acc":
            acc += int(b)
        instruction +=1


    return acc


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
