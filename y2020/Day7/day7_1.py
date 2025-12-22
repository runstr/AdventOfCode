import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
import re

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    rules = {}
    all_bags = set()
    gold_bag_parrents = []
    for rule in data:
        rule = re.sub(r"[\d] ", "", rule)[:-1]
        rule = re.sub(r"bag(?=$|\s|,)", "bags", rule)
        a, b = rule.split(" contain ")
        contains = b.split(", ")
        if "shiny gold bags" in contains:
            gold_bag_parrents.append(a)
        rules[a] = contains
    while gold_bag_parrents:
        parent = gold_bag_parrents.pop()
        all_bags.add(parent)
        for key, value in rules.items():
            if parent in value :
                gold_bag_parrents.append(key)


    print(all_bags)
    return len(all_bags)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
