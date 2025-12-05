import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    box_map = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "@":
                box_map.append((x,y))
    dxs=[-1,0,1]
    dys=[-1,0,1]
    count=0
    access = []
    for box in box_map:
        closest = 0
        for dy in dys:
            for dx in dxs:
                if dx ==0 and dy ==0:
                    continue
                new_x = box[0]+dx
                new_y = box[1]+dy
                if new_x >= len(data[0]) or new_y >= len(data) or new_x < 0 or new_y < 0:
                    continue
                if data[new_y][new_x] == "@":
                    closest+=1
        if closest <4:
            count+=1
            access.append((box[0], box[1]))
    return count


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
