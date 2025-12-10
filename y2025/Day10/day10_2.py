import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
import numpy as np
from scipy.optimize import linprog
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    machines = []
    for line in data:
        a = line.split(" ")
        final=np.array(list(map(int,a[-1][1:-1].split(","))))
        commands = []
        for b in a[1:-1]:
            numbers = list(map(int, b[1:-1].split(",")))
            command = [1 if i in numbers else 0 for i in range(len(final))]
            commands.append(command)
        machines.append((final, commands))

    total = 0
    for final, commands in machines:
        lhs_eq = np.transpose(commands)
        rhs_eq = final.tolist()
        objective = [1]*len(lhs_eq[0])
        opt = linprog(c=objective, A_eq = lhs_eq, b_eq = rhs_eq, method = "highs", integrality=1)
        total+= opt.fun
    return total


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
