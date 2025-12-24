import pathlib
import re

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def evaluate(string):
    numbers = list(map(int,re.findall(r'\d+', string)))
    operators = re.findall("[*+]", string)
    total_sum =numbers[0]
    for i in range(0, len(operators)):
        total_sum = eval(str(total_sum)+str(operators[i])+str(numbers[i+1]))
    return total_sum


def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    all_sums = []
    for line in lines:
        line = line.replace(" ", "")
        new_string = line
        while "(" in new_string:
            for i, char in enumerate(new_string):
                if char == "(":
                    start_index = i
                if char == ")":
                    end_index = i
                    break
            total_sum = evaluate(new_string[start_index+1:end_index])
            new_string = new_string[:start_index] + str(total_sum) + new_string[end_index+1:]
        all_sums.append(evaluate(new_string))
    return sum(all_sums)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
