import pathlib

from numpy.ma.core import maximum

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
from matplotlib import pyplot as plt
import numpy as np

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
def get_area(x1, y1, x2, y2):
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)

def distance(a, b):
    return (b[0]-a[0])**2+(b[1]-a[1])**2

def verify_no_points_inside(a, b, points):
    for point in points:
        if point[0]>min(a[0], b[0]) and point[0]<max(a[0], b[0]) and point[1]>min(a[1], b[1]) and point[1]<max(a[1], b[1]):
            return False
    return True

def plot_points(data, a, b):
    pts = np.array([tuple(map(int, line.split(","))) for line in data])
    xs, ys = zip(*pts)
    plt.plot(xs, ys, marker='o')
    point1 = a
    point2 = (b[0], a[1])
    point3 = b
    point4 = (a[0], b[1])
    rectangle_xs = [point1[0], point2[0], point3[0], point4[0], point1[0]]
    rectangle_ys = [point1[1], point2[1], point3[1], point4[1], point1[1]]
    plt.plot(rectangle_xs, rectangle_ys, marker='o', color='green')
    area = get_area(a[0], a[1], b[0], b[1])
    plt.title("Area: {}".format(area))
    plt.show()
    plt.close()

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    plotting_on = False
    points=[]
    for line in data:
        x1, y1 = map(int, line.split(","))
        points.append((x1, y1))
    longest_distance_1 = (0, 0, 0)
    longest_distance_2 = (0, 0, 0)
    for i in range(0, len(data)-1):
        dist = distance(points[i], points[i+1])
        if dist > longest_distance_1[0]:
            longest_distance_2 = longest_distance_1
            longest_distance_1 = (dist, i, i+1)
        elif dist > longest_distance_2[0]:
            longest_distance_2 = (dist, i, i+1)
    start_point_1 = points[longest_distance_1[2]]
    start_point_2 = points[longest_distance_2[1]]
    start_counting_first = False
    start_counting_second = False
    maximum_area = 0
    calculating = False
    for point in points:
        if point[0]<start_point_1[0] and start_counting_first:
            start_counting_first = False
            start_counting_second = True
            temp_point = point
        if point[0]>start_point_1[0] and not start_counting_second:
            start_counting_first = True
        if start_counting_second and point[1] < temp_point[1]:
            start_counting_second  =False
            calculating = True
        if calculating:
            area = get_area(start_point_1[0], start_point_1[1], point[0], point[1])
            if point[1]<=start_point_1[1]:
                break
            if area > maximum_area:
                if verify_no_points_inside(start_point_1, point, points):
                    maximum_area = area
                    if plotting_on:
                        plot_points(data, start_point_1, point)

    start_counting_first = False
    start_counting_second = False
    calculating = False
    for point in reversed(points):
        if point[0]<start_point_2[0] and start_counting_first:
            start_counting_first = False
            start_counting_second = True
            temp_point = point
        if point[0]>start_point_2[0] and not start_counting_second:
            start_counting_first = True
        if start_counting_second and point[1] > temp_point[1]:
            start_counting_second  =False
            calculating = True
        if calculating:
            area = get_area(start_point_2[0], start_point_2[1], point[0], point[1])
            if point[1]>=start_point_2[1]:
                break
            if area > maximum_area:
                if verify_no_points_inside(start_point_1, point, points):
                    maximum_area = area
                    if plotting_on:
                        plot_points(data, start_point_1, point)

    return maximum_area

def bruteforce():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    points = []
    for line in data:
        x1, y1 = map(int, line.split(","))
        points.append((x1, y1))
    total_points = set()
    for i in range(len(points)-1):
        x_diff = abs(points[i+1][0]-points[i][0])
        y_diff = abs(points[i+1][1]-points[i][1])
        if x_diff==0:
            for y in range(min(points[i][1], points[i+1][1]), max(points[i][1], points[i+1][1])+1):
                total_points.add((points[i][0], y))
        elif y_diff==0:
            for x in range(min(points[i][0], points[i+1][0]), max(points[i][0], points[i+1][0])+1):
                total_points.add((x, points[i][1]))

    total_points = list(total_points)
    maximum_area=0
    for i in range(0, len(points)-1):
        for j in range(i, len(points)):
            a = points[i]
            b = points[j]
            area = get_area(a[0], a[1], b[0], b[1])
            if area>maximum_area:
                if verify_no_points_inside(a, b, total_points):
                    maximum_area = area
    return maximum_area



@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
