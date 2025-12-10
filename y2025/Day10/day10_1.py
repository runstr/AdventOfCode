import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    machines = []
    for line in data:
        a = line.split(" ")
        final=a[0][1:-1]
        commands = []
        final = "".join(["1" if i=="#" else "0" for i in final])
        for b in a[1:-1]:
            numbers = list(map(int, b[1:-1].split(",")))
            command = ["1" if i in numbers else "0" for i in range(len(final))]
            binary_command = "".join(command)
            commands.append(int(binary_command,2))
        final = int(final,2)
        machines.append((final, commands))
    total_visits = 0
    for i, machine in enumerate(machines):
        final_number = machine[0]
        og_commands = machine[1]
        next_commands=[]
        finished = False
        new_total_presses=0
        for number in machine[1]:
            if number == final_number:
                new_total_presses = 1
                finished = True
                break
            next_commands.append((number, 1, {number}))
        while next_commands:
            this_number, total_presses, visited = next_commands.pop(0)
            for next_c in og_commands:
                if next_c in visited:
                    break
                new_number = this_number ^ next_c
                new_total_presses = total_presses + 1
                new_visited = visited.union({next_c})
                if new_number == final_number:
                    finished = True
                    break
                next_commands.append((new_number, new_total_presses, new_visited))
            if finished:
                break
        total_visits+=new_total_presses


    return total_visits


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
