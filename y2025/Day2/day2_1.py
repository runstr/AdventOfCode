import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()


def get_my_answer():
    data = load_data(filepath, example=False)
    sequences = data.split(",")
    invalid_ids = []
    for sequence in sequences:
        first, second = map(int, sequence.split("-"))
        for i in range(first, second+1):
            number = str(i)
            a = len(number)//2
            if number[:a] == number[a:]:
                invalid_ids.append(i)
    return sum(invalid_ids)


@timeexecution
def execution():
    submit_answer = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
