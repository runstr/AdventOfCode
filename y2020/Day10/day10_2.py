import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit


filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def dfs(index, joltages, memory):
    if index in memory:
        return memory[index]
    if index == len(joltages)-1:
        return 1
    number = joltages[index]
    possible_numbers = []
    for i in range(1,4):
        if index+i < len(joltages) and joltages[index+i]<=number+3:
            possible_numbers.append(index+i)
    total=0
    for possible_number in possible_numbers:
        total+=dfs(possible_number, joltages, memory)
    memory[index] = total
    return total


def get_my_answer():
    joltages = list(map(int,(load_data_as_lines(filepath, example=EXAMPLE))))
    joltages.sort()
    joltages =[0] + joltages + [joltages[-1] + 3]
    total = dfs(0, joltages,{})
    return total





    return


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
