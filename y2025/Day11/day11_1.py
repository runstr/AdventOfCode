import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    hash_map ={}
    for line in data:
        start, endpoints = line.split(": ")
        endpoints = endpoints.split(" ")
        hash_map[start] = endpoints
    next_point=[("you", set())]
    total_visits =0
    while next_point:
        point, visited = next_point.pop()
        for endpoint in hash_map[point]:
            if endpoint == "out":
                total_visits+=1
                continue
            if endpoint not in visited:
                new_visited = visited.copy()
                new_visited.add(endpoint)
                next_point.append((endpoint, new_visited))
    return total_visits


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
