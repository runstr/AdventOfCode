import pathlib

import numpy as np

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def check_number(number, rules):
    for rule in rules:
        if rule[0]<=number<=rule[1]:
            return True
    return False

def get_my_answer():
    data= load_data(filepath, example=EXAMPLE)
    nearby_tickets = [list(map(int,a.split(","))) for a in data.split("nearby tickets:\n")[1].split("\n")]
    my_ticket = list(map(int,data.split("\n\nyour ticket:")[1].split("\n")[1].split(",")))
    rules = [a.split(": ") for a in data.split("\n\nyour ticket:")[0].split("\n")]
    new_rules = {}
    for rule in rules:
        a= tuple(map(int,rule[1].split(" or ")[0].split("-")))
        b= tuple(map(int,rule[1].split(" or ")[1].split("-")))
        new_rules[rule[0]]=[a,b]
    invalid_tickets = set()
    all_rules = []
    for value in new_rules.values():
        all_rules.append(value[0])
        all_rules.append(value[1])
    for i, ticket in enumerate(nearby_tickets):
        for number in ticket:
            if not check_number(number, all_rules):
                invalid_tickets.add(i)
    valid_tickets  = []
    for i in range(len(nearby_tickets)):
        if i not in invalid_tickets:
            valid_tickets.append(nearby_tickets[i])
    columns = np.transpose(valid_tickets)
    mapping = []
    for key, values in new_rules.items():
        valid_mappings = []
        for i, column in enumerate(columns):
            found = True
            for j in column:
                if not check_number(j, values):
                    found = False
                    break
            if found:
                valid_mappings.append(i)
        mapping.append((key, valid_mappings))
    mapping.sort(key=lambda x: len(x[1]))
    last_mapping = set()
    unique_mappings = []
    departure = []
    for val in mapping:
        unique_mappings.append((val[0], set(val[1])-last_mapping))
        if "departure" in val[0]:
            departure.append(list(set(val[1])-last_mapping)[0])
        last_mapping = set(val[1])
    sum = 1
    for row in departure:
        sum*=my_ticket[row]
    return sum







@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
