import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

from y2024.Day7.day7_2 import check_number

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False
def check_number(number, rules):
    for rule in rules:
        if rule[0]<=number<=rule[1]:
            return True
    return False

def get_my_answer():
    data= load_data(filepath, example=EXAMPLE)
    nearby_tickets = [list(map(int,a.split(","))) for a in data.split("nearby tickets:\n")[1].split("\n")]
    rules = [a.split(": ")[1] for a in data.split("\n\nyour ticket:")[0].split("\n")]
    new_rules = []
    for rule in rules:
        first, second = rule.split(" or ")
        minimum = first.split("-")[0]
        maximum = first.split("-")[1]
        new_rules.append((int(minimum), int(maximum)))
        minimum = second.split("-")[0]
        maximum = second.split("-")[1]
        new_rules.append((int(minimum), int(maximum)))
    invalid_numbers = []
    for ticket in nearby_tickets:
        for number in ticket:
            if not check_number(number, new_rules):
                invalid_numbers.append(number)
    return sum(invalid_numbers)



@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
