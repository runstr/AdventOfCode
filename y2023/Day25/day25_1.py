import math
import pathlib
from copy import copy
import networkx as nx

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()


def get_my_answer():
    data = load_data_as_lines(filepath, example=False)
    nodes = {}
    graph = nx.Graph()
    start_node = "zzn"
    end_node = "zkb"
    for line in data:
        start, ends = line.split(": ")
        ends = ends.split(" ")
        for end in ends:
            graph.add_edge(start, end, weight=1.0)
        if start in nodes:
            nodes[start] += [*ends]
        else:
            nodes[start] = [*ends]
        for end_node in ends:
            if end_node in nodes:
                nodes[end_node] += [start]
            else:
                nodes[end_node] = [start]
    min_cut, partition = nx.stoer_wagner(graph)
    print(min_cut, len(partition[0]), len(partition[1]))
    return

def find_minimum_path(start_node, nodes):
    next_node = [(start_node, length)]


@timeexecution
def execution():
    submit_answer = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=2023)
