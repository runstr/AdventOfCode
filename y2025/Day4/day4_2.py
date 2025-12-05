import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_closets(box_map, data):
    count = 0
    access = []
    ds = [(-1, 0), (1, 0), (0, 1), (0,-1), (1, 1), (-1,-1)]
    for box in box_map:
        closest = 0
        for dx, dy in ds:
            new_x = box[0] + dx
            new_y = box[1] + dy
            if new_x >= len(data[0]) or new_y >= len(data) or new_x < 0 or new_y < 0:
                continue
            if data[new_y][new_x] == "@":
                closest += 1
        if closest < 4:
            count += 1
            access.append((box[0], box[1]))
    return access

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    box_map = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "@":
                box_map.append((x, y))
    total_removed = 0
    while True:
        closest = get_closets(box_map,data)
        if len(closest) ==0:
            break
        for box in closest:
            box_map.remove(box)
            data[box[1]] = data[box[1]][:box[0]]+"."+data[box[1]][box[0]+1:]
            total_removed+=1

    return total_removed


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
