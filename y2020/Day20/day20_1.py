import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False


def match_values(line, values):
    line1 = (values[0], False, (1,0))
    line2 = (line1[0][::-1], True, (1,0))
    line3 = (values[len(values) -1], False, (-1,0))
    line4 = (line3[0][::-1], True, (-1,0))
    line5 = ("".join([a[0] for a in values]), False, (0, -1))
    line6 = (line5[0][::-1], True, (0, -1))
    line7 = ("".join([a[len(a)-1] for a in values]), False, (0,1))
    line8 = (line7[0][::-1], True, (0, 1))
    test_lines = [line1, line2, line3, line4, line5, line6, line7, line8]
    for test, flipped, dir in test_lines:
        if test == line:
            return 1

    return 0



def get_my_answer():
    data = load_data(filepath, example=EXAMPLE).split("\n\n")
    tiles = {}
    for tile in data:
        a = tile.split("\n")[0]
        b = tile.split("\n")[1:]
        tiles[a] = b
    all_matches = {}
    for key, values in tiles.items():
        matches=0
        for key2, values2 in tiles.items():
            if key2 == key:
                continue
            line1 = values[0]
            line3 = values[len(values) - 1]
            line5 = "".join([a[0] for a in values])
            line7 = "".join([a[len(a) - 1] for a in values])
            total_matches = 0
            for line in [line1,line3,line5,line7]:
                total_matches += match_values(line, values2)
            matches += total_matches
        all_matches[key] = matches
    sum = 1
    for key, values in all_matches.items():
        if values == 2:
            print(key, values)
            sum *=int(key[-5:-1])




    return all_matches

def print_map(value):
    for line in value:
        print(line)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
