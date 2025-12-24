import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False


def get_my_answer():
    rs, messages = load_data(filepath, example=EXAMPLE).split("\n\n")
    rules = {}
    for r in rs.split("\n"):
        a,b = r.split(": ")
        rules[a] = b.replace('"', "")
    next_rules = ["0"]
    """
    while True:
        next_rule = next_rules.pop()
        new_rules = []
        for i in next_rule.split(" "):
            a = rules[i]
            if "|" in a:
                b,c = a.split(" | ")
            else:
                next_rules.append(a)"""



@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
