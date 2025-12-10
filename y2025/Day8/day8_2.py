import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
import math
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False


def shortest_distance(a, b):
    return math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2+(b[2]-a[2])**2)

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    points = []
    for line in data:
        x, y, z = line.split(",")
        points.append(tuple(map(int, (x, y, z))))
    connections = []
    path_distances = []
    for i in range(0, len(points)-1):
        for j in range(i+1, len(points)):
            a = points[i]
            b = points[j]
            if (i, j) in connections:
                continue
            minimum = shortest_distance(a, b)
            path_distances.append((minimum, a,b))
    path_distances.sort()
    connections = {}
    circuits = 0
    final_points = None
    remaining_points = set(points)
    for index, path in enumerate(path_distances):
        _, a, b = path
        a_in = None
        b_in = None
        for key, value in connections.items():
            if b in value:
                b_in = key
            elif a in value:
                a_in = key
            if a_in and b_in:
                break
        if a_in is not None and b_in is None:
            connections[a_in].add(b)
            remaining_points.discard(b)
        elif a_in is None and b_in is not None:
            connections[b_in].add(a)
            remaining_points.discard(a)
        elif a_in is not None and b_in is not None:
            connections[a_in] = connections[a_in].union(connections[b_in])
            connections.pop(b_in)
        else:
            remaining_points.discard(a)
            remaining_points.discard(b)
            connections[circuits] = {a, b}
            circuits += 1
        if len(connections) == 1 and not remaining_points:
            final_points = (a,b)
            break
    return final_points[0][0]*final_points[1][0]


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
