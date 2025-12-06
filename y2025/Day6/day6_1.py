import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    columns =[]
    new_lines = []
    for line in lines:
        test = line.split(" ")
        new_line = []
        for a in test:
            if a.isdigit():
                new_line.append(int(a))
            elif a in ["*", "+"]:
                new_line.append(a)
        new_lines.append(new_line)
    total_sum = 0
    for i in range(len(new_lines[0])):
        if new_lines[-1][i] =="*":
            temp_sum = 1
        else:
            temp_sum=0
        for j in range(len(new_lines[:-1])):
            if new_lines[-1][i] =="*":
                temp_sum *= new_lines[j][i]
            else:
                temp_sum += new_lines[j][i]
        total_sum+=temp_sum
    return total_sum


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
