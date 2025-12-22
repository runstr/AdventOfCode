import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = True

def update_direction(dx,dy, turn):
    if turn == "L90" or turn == "R270":
        dx, dy = -dy, dx
    elif turn == "R90" or turn == "L270":
        dx, dy = dy, -dx
    elif turn == "L180" or turn == "R180":
        dx, dy =-dx, -dy
    return dx, dy

def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    dx, dy = 10, 1
    x, y = 0, 0
    for line in lines:
        if "R" in line or "L" in line:
            dx, dy = update_direction(dx, dy, line)
        elif "F" in line:
            x += dx*int(line[1:])
            y += dy*int(line[1:])
        elif "N" in line:
            dy += int(line[1:])
        elif "S" in line:
            dy -= int(line[1:])
        elif "E" in line:
            dx += int(line[1:])
        elif "W" in line:
            dx -= int(line[1:])
        #print(x,y,dx,dy)
    return abs(x) + abs(y)



@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
