import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution, load_data_as_map
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    full_map, max_x, max_y = load_data_as_map(filepath, example=EXAMPLE)
    asteroids =[]
    for key, value in full_map.items():
        if value == "#":
            asteroids.append(key)
    all_asteroids = {}
    for asteroid1 in asteroids:
        all_vectors = set()
        for asteroid2 in asteroids:
            if asteroid1 != asteroid2:
                vector = (asteroid2[0]-asteroid1[0], asteroid2[1]-asteroid1[1])
                x = vector[0]
                y = vector[1]
                x1=x / math.gcd(abs(x), abs(y))
                y1=y / math.gcd(abs(x), abs(y))
                all_vectors.add((x1,y1))
        all_asteroids[asteroid1] = all_vectors
    maximum = 0
    asteroid = None
    for key,value in all_asteroids.items():
        if len(value)>maximum:
            maximum = len(value)
            asteroid = key
    return maximum, asteroid


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
