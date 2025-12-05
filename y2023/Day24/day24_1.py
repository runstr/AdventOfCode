import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()

def calculate_line(point, velocity):
    a = velocity[1]/velocity[0]
    b = point[1]-a*point[0]
    return (a, b)

def get_interception_point(line1, point1, velocity1, line2, point2, velocity2):
    """
    a1x+b1=y => a1x+b1 = a2x+b2 => a1x-a2x+ = b2-+b1
    :param line1:
    :param line2:
    :return:
    """
    if line1[0]==line2[0]:
        return None
    x_point = (line2[1]-line1[1])/(line1[0]-line2[0])
    y_point = line1[0]*x_point+line1[1]
    if velocity1[0]>0 and x_point<point1[0] or velocity1[0]<0 and x_point>point1[0]:
        return None
    if velocity2[0]>0 and x_point<point2[0] or velocity2[0]<0 and x_point>point2[0]:
        return None
    if velocity1[1]>0 and y_point<point1[1] or velocity1[1]<0 and y_point>point1[1]:
        return None
    if velocity2[1]>0 and y_point<point2[1] or velocity2[1]<0 and y_point>point2[1]:
        return None
    return x_point, y_point

def get_my_answer():
    example = False
    data = load_data_as_lines(filepath, example=example)
    points = []
    lines = []
    velocities = []
    for line in data:
        point, velocity = line.split(" @ ")
        point = tuple(map(int, point.split(", ")))
        velocity = tuple(map(int, velocity.split(", ")))
        points.append(point)
        velocities.append(velocity)
        lines.append(calculate_line(point[0:2], velocity[0:2]))
    allowed_interceptions = 0
    if example:
        min_x = min_y = 7
        max_x = max_y = 27
    else:
        min_x = min_y = 200000000000000
        max_x = max_y = 400000000000000
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            intersection_point = get_interception_point(lines[i], points[i], velocities[i], lines[j], points[j], velocities[j])
            if intersection_point is not None:
                x_point, y_point = intersection_point
            else:
                continue
            if min_x < x_point<max_x and min_y < y_point<max_y:
                allowed_interceptions += 1

    return allowed_interceptions


@timeexecution
def execution():
    submit_answer = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=2023)
