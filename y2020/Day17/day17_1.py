import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, load_data_as_map, timeexecution
from aocd import submit
from matplotlib import pyplot as plt

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = True

def check_closets_neighbours(x,y,z, active):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if (x+dx, y+dy, z+dz) in active:
                    count += 1
    return count

def plot_map(points):
    from collections import defaultdict

    # Group by z
    by_z = defaultdict(set)
    for x, y, z in points:
        by_z[z].add((x, y))

    # Global XY bounds
    xs = [x for x, y, z in points]
    ys = [y for x, y, z in points]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Render slices
    for z in sorted(by_z):
        print(f"\nZ = {z}")

        # Empty grid
        grid = [["." for _ in range(width)] for _ in range(height)]

        # Plot points
        for x, y in by_z[z]:
            grid[y - min_y][x - min_x] = "c"

        # Print TOP → BOTTOM (screen coordinates)
        for row in grid:
            print("".join(row))


def get_my_answer():
    data= load_data_as_lines(filepath, example=EXAMPLE)
    active = set()
    max_x = len(data[0])
    max_y = len(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                active.add((x,y,0))
    num_cycles = 6
    for i in range(num_cycles):
        new_active = set()
        for x in range(-num_cycles, max_x+num_cycles+1):
            for y in range(-num_cycles, max_y+num_cycles+1):
                for z in range(-num_cycles, num_cycles+1):
                    count = check_closets_neighbours(x,y,z,active)
                    if (x,y,z) in active and (count == 2 or count == 3):
                        new_active.add((x,y,z))
                    elif ((x,y,z) not in active) and count == 3:
                        new_active.add((x,y,z))

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
        submit(my_answer, part="a", day=this_day, year=this_year)
