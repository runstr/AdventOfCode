import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
from sympy import Eq, symbols, solve, solve_linear
filepath = pathlib.Path(__file__).parent.resolve()

def get_equations(point1, point2, point3):
    xs, ys, zs, dxs, dys, dzs, x1, y1, z1, x2, y2, z2, x3, y3, z3, t1, t2, t3 = symbols("xs, ys, zs, dxs, dys, dzs, x1, y1, z1, x2, y2, z2, x3, y3, z3, t1, t2, t3")
    eq1 = Eq(point1[0][0] + point1[1][0] * t1, x1)
    eq2 = Eq(point1[0][1] + point1[1][1] * t1, y1)
    eq3 = Eq(point1[0][2] + point1[1][2] * t1, z1)
    eq4 = Eq(xs + dxs * t1, x1)
    eq5 = Eq(ys + dys * t1, y1)
    eq6 = Eq(zs + dzs * t1, z1)

    eq7 = Eq(point2[0][0] + point2[1][0] * t2, x2)
    eq8 = Eq(point2[0][1] + point2[1][1] * t2, y2)
    eq9 = Eq(point2[0][2] + point2[1][2] * t2, z2)
    eq10 = Eq(xs + dxs * t2, x2)
    eq11 = Eq(ys + dys * t2, y2)
    eq12 = Eq(zs + dzs * t2, z2)

    eq13 = Eq(point3[0][0] + point3[1][0] * t3, x3)
    eq14 = Eq(point3[0][1] + point3[1][1] * t3, y3)
    eq15 = Eq(point3[0][2] + point3[1][2] * t3, z3)
    eq16 = Eq(xs + dxs * t3, x3)
    eq17 = Eq(ys + dys * t3, y3)
    eq18 = Eq(zs + dzs * t3, z3)
    result = solve([eq1, eq2, eq3, eq4,eq5, eq6, eq7, eq8,  eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16, eq17, eq18], xs, ys, zs, dxs, dys, dzs, x1, y1, z1, x2, y2, z2, x3, y3, z3, t1, t2, t3)
    return result[0]
def get_my_answer():
    example = False
    data = load_data_as_lines(filepath, example=example)
    points = []
    for line in data:
        point, velocity = line.split(" @ ")
        point = tuple(map(int, point.split(", ")))
        velocity = tuple(map(int, velocity.split(", ")))
        points.append((point, velocity))
    results = get_equations(points[0], points[1], points[2])
    print(sum((results[0], results[1], results[2])))

    return results


@timeexecution
def execution():
    submit_answer = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=2023)
