import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution, load_data_as_map
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def find_asteroids(start_asteroid, asteroids):
    all_vectors = {}
    for asteroid in asteroids:
        if start_asteroid == asteroid:
            continue
        vector = (asteroid[0]-start_asteroid[0], asteroid[1]-start_asteroid[1])
        x=vector[0] / math.gcd(abs(vector[0]), abs(vector[1]))
        y=vector[1] / math.gcd(abs(vector[0]), abs(vector[1]))
        angle = math.degrees(math.atan2(x, -y))
        if angle<0:
            angle+=360
        length = math.sqrt(vector[0]**2 + vector[1]**2)
        if angle in all_vectors:
            all_vectors[angle].append((length, asteroid))
        else:
            all_vectors[angle] = [(length, asteroid)]
    return all_vectors

def get_my_answer():
    full_map, max_x, max_y = load_data_as_map(filepath, example=EXAMPLE)
    asteroids = set()
    for key, value in full_map.items():
        if value == "#":
            asteroids.add(key)
    if EXAMPLE:
        best_asteroid = (11,13)
    else:
        best_asteroid = (22, 19) # From part 1
    all_asteroids = find_asteroids(best_asteroid, asteroids)
    for key, value in all_asteroids.items():
        value.sort()
        all_asteroids[key] = value
    all_angles = list(all_asteroids.keys())
    all_angles.sort()
    i=0
    destroyed = 0
    while True:
        angle = all_angles[i%len(all_angles)]
        asteroid = all_asteroids[angle]
        if asteroid:
            a = asteroid.pop(0)
            destroyed+=1

        if destroyed==200:
            break
        i+=1
    return a[1][0]*100+a[1][1]

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
