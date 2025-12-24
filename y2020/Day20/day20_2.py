import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def flip(matrix, dir):
    if dir == -1:
        return [row[::-1] for row in matrix]
    else:
        return matrix[::-1]

def rotate(matrix, degrees):
    n = len(matrix)

    if degrees == 90:
        return [row[::-1] for row in matrix[::-1]]

    elif degrees == 180:
        return [
            "".join(matrix[n - 1 - r][c] for r in range(n))
            for c in range(n)
        ]
    elif degrees == 270:
        return [
            "".join(matrix[r][n - 1 - c] for r in range(n))
            for c in range(n - 1, -1, -1)
        ]

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
            return flipped, dir
    return False


def get_my_answer():
    data = load_data(filepath, example=EXAMPLE).split("\n\n")
    tiles = {}
    for tile in data:
        a = tile.split("\n")[0]
        b = tile.split("\n")[1:]
        tiles[a] = b
    if EXAMPLE:
        next_tile = "Tile 1951:"
    else:
        next_tile = "Tile 2789:"
    next_tiles = [next_tile]
    placed = set()
    maps = {}
    while next_tiles:
        next_tile = next_tiles.pop()
        placed.add(next_tile)
        new_map = tiles[next_tile]
        line1 = (new_map[0], (1, 0))
        line3 = (new_map[len(new_map) - 1], (-1, 0))
        line5 = ("".join([a[0] for a in new_map]), (0, -1))
        line7 = ("".join([a[len(a) - 1] for a in new_map]), (0, 1))
        connections = []
        for key, value in tiles.items():
            if key == next_tile:
                continue
            for line, dir in [line1, line3, line5, line7]:
                test = match_values(line, value)
                if not test:
                    continue
                else:
                    break
            if test:
                if key not in placed:
                    next_tiles.append(key)
                connections.append((key, dir, test[0], test[1]))
        maps[next_tile] = connections
    for key, value in maps.items():
        print(key, value)
    return


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
