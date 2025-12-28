import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
opcodes = {
    "1": "+",
    "2": "*",
    "3": "input",
    "4": "output",
    "99": "exit"}

def get_my_answer():
    data = list(map(int,load_data(filepath, example=EXAMPLE).split(",")))
    next_instruction = 0
    input = 1
    outputs = []
    while True:
        opcode = str(data[next_instruction])
        opcode = "0" * (5 - len(opcode)) + opcode
        instruction = int(opcode[-2:])
        first, second, third = int(opcode[-3]),int(opcode[-4]), int(opcode[-5])
        match instruction:
            case 99:
                break
            case 3:
                first_val = next_instruction + 1 if first else data[next_instruction + 1]
                data[first_val] = input
                next_instruction += 2
                continue
            case 4:
                first_val = next_instruction + 1 if first else data[next_instruction + 1]
                outputs.append(int(data[first_val]))
                next_instruction += 2
                continue
            case 1:
                first_val = data[next_instruction + 1] if first else data[data[next_instruction + 1]]
                second_val = data[next_instruction + 2] if second else data[data[next_instruction + 2]]
                third_val = next_instruction + 3 if third else data[next_instruction + 3]
                data[third_val] = first_val+second_val
                next_instruction += 4
            case 2:
                first_val = data[next_instruction + 1] if first else data[data[next_instruction + 1]]
                second_val = data[next_instruction + 2] if second else data[data[next_instruction + 2]]
                third_val = next_instruction + 3 if third else data[next_instruction + 3]
                data[third_val] = first_val*second_val
                next_instruction += 4
    return outputs[-1]

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
