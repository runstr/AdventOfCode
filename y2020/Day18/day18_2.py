import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
import re
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def evaluate(string):
    numbers = re.findall(r'[\d]+|[*+]', string)
    new_numbers = []
    i=0
    while i < len(numbers):
        if numbers[i]=="+":
            new_numbers[-1] = str(eval(new_numbers[-1]+"+"+numbers[i+1]))
            i=i+1
        else:
            new_numbers.append(numbers[i])
        i=i+1
    return eval("".join(new_numbers))



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
        submit(my_answer, part="b", day=this_day, year=this_year)
