import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    all_nodes = {}
    for line in data:
        a,b = line.split(")")
        if a in all_nodes:
            all_nodes[a].append(b)
        else:
            all_nodes[a] = [b]
    nodes = [("", "COM")]
    parent_nodes = {}
    while nodes:
        parent_node, node = nodes.pop()
        if node in all_nodes:
            next_nodes = all_nodes[node]
        else:
            continue
        for n in next_nodes:
            a = parent_node + "-" + node
            nodes.append((a, n))
            parent_nodes[n] = a
    total_indirect_orbits = 0
    for key, value in parent_nodes.items():
        total_indirect_orbits += (len(value[1:].split("-")))
    return total_indirect_orbits


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
