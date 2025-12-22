import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def check_closets_neighbours(x, y, z, w, active):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if (x+dx, y+dy, z+dz, w+dw) in active:
                        count += 1
    return count


def get_my_answer():
    data= load_data_as_lines(filepath, example=EXAMPLE)
    active = set()
    max_x = len(data[0])
    max_y = len(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                active.add((x,y,0,0))
    num_cycles = 6
    for i in range(num_cycles):
        new_active = set()
        for x in range(-num_cycles, max_x+num_cycles+1):
            for y in range(-num_cycles, max_y+num_cycles+1):
                for z in range(-num_cycles, num_cycles+1):
                    for w in range(-num_cycles, num_cycles+1):
                        count = check_closets_neighbours(x,y,z,w,active)
                        if (x,y,z,w) in active and (count == 2 or count == 3):
                            new_active.add((x,y,z,w))
                        elif ((x,y,z,w) not in active) and count == 3:
                            new_active.add((x,y,z,w))

        active = new_active

    return len(active)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
