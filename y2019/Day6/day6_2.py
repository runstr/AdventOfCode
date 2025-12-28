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
        if b in all_nodes:
            all_nodes[b].append(a)
        else:
            all_nodes[b] = [a]
    nodes = [("YOU", 0)]
    visited = set()
    while nodes:
        node, moves = nodes.pop()
        if node == "SAN":
            return moves -2
        if node in all_nodes:
            next_nodes = all_nodes[node]
        else:
            continue
        visited.add(node)
        for n in next_nodes:
            if n not in visited:
                nodes.append((n, moves + 1))

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
