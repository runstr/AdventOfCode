import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    instructions = load_data_as_lines(filepath, example=EXAMPLE)
    for i in range(1, len(instructions)):
        if instructions[i].split()[0] == "nop":
            new_instructions = [a for a in instructions]
            new_instructions[i] = new_instructions[i].replace("nop", "jmp")
        elif instructions[i].split()[0] == "jmp":
            new_instructions = [a for a in instructions]
            new_instructions[i] = new_instructions[i].replace("jmp", "nop")
            pass
        else:
            continue
        found_correct = False
        instruction = 0
        visited = set()
        acc = 0
        while True:
            if instruction in visited:
                break
            if instruction == len(new_instructions):
                found_correct = True
                break
            visited.add(instruction)
            current = new_instructions[instruction]
            a, b = current.split(" ")
            if a =="jmp":
                instruction+= int(b)
                continue
            elif a == "acc":
                acc += int(b)
            instruction +=1
        if found_correct:
            break
    return acc


def get_my_answer_faster():
    """
    Here we implement a directed graph. First we implent a graph on how we get to each point.
    So to get to point x we did either jmp or instruction +1
    After this we traverse backwards from endpoint which is directly after the last instruction. So we append to a set all points
    on this reverse graph.
    After this we know that if we can get to one of these points by doing a change in instruction that leads to these
    points, we can continue to the end from there
    :return:
    """
    instructions = load_data_as_lines(filepath, example=EXAMPLE)
    # first find graph
    graph = {}
    for i, instruction in enumerate(instructions):
        a, b = instruction.split(" ")
        if a == "nop" or a == "acc":
            next = i+1
        else:
            next = i+int(b)
        if next in graph:
            graph[next].append(i)
        else:
            graph[next] = [i]
    endpoints = [len(instructions)]
    points = set()
    visited = set()
    # Traverse backwards to find all points that can lead to the endpoint
    while endpoints:
        N = endpoints.pop()
        points.add(N)
        visited.add(N)
        if N in graph:
            next_points = graph[N]
        else:
            continue
        for point in next_points:
            if point not in visited:
                endpoints.append(point)

    instruction = 0
    acc=0
    while instruction<len(instructions):
        current = instructions[instruction]
        a, b = current.split(" ")
        if a =="jmp":
            if instruction+1 in points:
                instruction += 1
                # Make sure we don't do any more changes
                points = set()
            else:
                instruction+= int(b)
        elif a == "nop":
            if instruction+int(b) in points:
                instruction += int(b)
                # Make sure we don't do any more changes
                points = set()
            else:
                instruction+=1
        else:
            acc += int(b)
            instruction +=1
    return acc





@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer_faster()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
