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
        for num in range(first, second+1):
            number = str(num)
            test_sequence = ""
            for index in range(0, len(number)//2+1):
                test_sequence += number[index]
                mult = len(number) // len(test_sequence)
                if  test_sequence * int(mult) == number and mult !=1:
                    invalid_ids.append(int(number))
                    break
    return sum(invalid_ids)


@timeexecution
def execution():
    SUBMIT_ANSWER = False
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
