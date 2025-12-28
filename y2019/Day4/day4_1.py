import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

def build_increasing_number(minimum, maximum):
    possible_numbers = [str(i) for i in range(int(minimum[0]), int(maximum[0]) + 1)]
    for i in range(1, 6):
        new_possible_numbers = []
        for possible_number in possible_numbers:
            for i in range(int(possible_number[-1]), 10):
                new_number = possible_number + str(i)
                if (int(minimum[:len(new_number)]) <= int(new_number)
                        <= int(maximum[:len(new_number)])):
                    new_possible_numbers.append(new_number)
        possible_numbers = new_possible_numbers
    return possible_numbers

def get_my_answer():
    minimum,maximum = load_data(filepath, example=EXAMPLE).split("-")
    possible_numbers = build_increasing_number(minimum, maximum)
    final_numbers=[]
    for number in possible_numbers:
        for j in range(len(number)-1):
            if number[j] == number[j+1]:
                final_numbers.append(number)
                break



    return len(final_numbers)


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
