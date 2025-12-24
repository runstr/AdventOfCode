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
    gold_bag_childs = []
    for rule in data:
        rule = re.sub(r"bag(?=$|\s|,|\.)", "bags", rule)[:-1]
        a, b = rule.split(" contain ")
        b = re.findall(r"(\d+)\s+([^,]+)", b)
        if "shiny gold bags" == a:
            gold_bag_childs = b
        rules[a] = b
    total_bags = 0
    while gold_bag_childs:
        num, parent = gold_bag_childs.pop(0)
        total_bags += int(num)
        try:
            childs = rules[parent]
        except KeyError:
            continue
        for child in childs:
            gold_bag_childs.append((str(int(child[0])*int(num)), child[1]))
    return total_bags


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
