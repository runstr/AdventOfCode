import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    groups = data.split("\n\n")
    total_yes = 0
    for group in groups:
        answers = group.split("\n")
        unique_yes = set(answers[0])
        for answer in answers[1:]:
            unique_yes = unique_yes.intersection(set(list(answer)))
        total_yes += len(unique_yes)
    return total_yes


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
