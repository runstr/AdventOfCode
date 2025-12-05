import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    total = 0
    for line in data:
        maximum_number = ""
        numbers = list(map(int, list(line)))
        max_index = -1
        total_num = 12
        for i in range(total_num-1, -1, -1):
            # Find the maximum number in the remaining sequence after max_index, but making sure there are enough numbers left to fill the remaining digits
            number_sequence = numbers[max_index + 1:len(numbers)-i]
            max_index = max_index+1+numbers[max_index+1:].index(max(number_sequence))
            maximum_number +=line[max_index]
        total+=int(maximum_number)
    return total


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
