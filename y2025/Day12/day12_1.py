import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    data = data.split("\n\n")
    areas = data[6].split("\n")
    pieces = []
    for piece in data[:6]:
        pieces.append(piece[3:].replace("\n", "").count("#"))
    count = 0
    full_areas = len(areas)
    for area in areas:
        a, b = area.split(": ")
        total_area = eval(a.replace("x", "*"))
        total_piece_area = 0
        for i, piece in enumerate(b.split(" ")):
            total_piece_area+= int(piece)*pieces[i]
        if total_piece_area<=total_area:
            count+=1



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
