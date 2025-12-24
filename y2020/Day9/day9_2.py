import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def check_validity(this_number, previous_number):
    for i in range(len(previous_number)-1):
        for j in range(i, len(previous_number)):
            if previous_number[i] + previous_number[j] == this_number:
                return True
    return False


def get_my_answer():
    numbers = list(map(int,load_data_as_lines(filepath, example=EXAMPLE)))
    preamble = 25
    for i in range(preamble, len(numbers)):
        previous_numbers = numbers[i-preamble:i]
        if not check_validity(numbers[i], previous_numbers):
            break
    final_number = numbers[i]
    total_numbers =[]
    j = 0
    total_sum = 0
    while j<len(numbers):
        if total_sum>final_number:
            total_sum-=total_numbers.pop(0)
            if total_sum == final_number:
                break
            continue
        total_numbers.append(numbers[j])
        total_sum += numbers[j]
        if total_sum==final_number:
            break
        j+=1


    return min(total_numbers)+max(total_numbers)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
