import functools
import pathlib
from functools import cache

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
hash_map ={}


def depth_search(key, endpoint, memory):
    if key in memory:
        return memory[key]
    total_visits = 0
    for next_point in hash_map[key]:
        if next_point == endpoint:
            total_visits += 1
            continue
        if next_point == "out":
            continue
        total_visits += depth_search(next_point, endpoint, memory)
    memory[key] = total_visits
    return total_visits

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    for line in data:
        start, endpoints = line.split(": ")
        endpoints = endpoints.split(" ")
        hash_map[start] = endpoints
    total_visits = depth_search("fft", "dac", {})*depth_search("svr", "fft", {})*depth_search("dac", "out", {})
    return total_visits


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
