import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    new_lines = lines[:-1]
    operators = [op for op in lines[-1].split(" ") if op != ""]
    total_sum = 0
    numbers = []
    print(new_lines)
    operator_index = 0
    max_length = max(len(new_lines[j]) for j in range(len(new_lines)))
    for j, line in enumerate(new_lines):
        if len(line) != max_length:
            new_length = max_length-len(line)
            new_lines[j] = line + (" "*(new_length))
        print(len(new_lines[j]))

    for i in range(max_length):
        new_number = ""
        for j in range(len(new_lines)):
            new_number+=new_lines[j][i]
        if new_number == " "*len(new_lines):
            this_sum = eval(operators[operator_index].join(numbers))
            operator_index += 1
            print(numbers)
            print(this_sum)
            total_sum += this_sum
            numbers = []
        else:
            numbers.append(new_number.strip(" "))
    print(numbers)
    total_sum+=eval(operators[operator_index].join(numbers))
    lines[-1].split()
    print(new_lines)


    """
    for i in range(len(new_lines[0])):
        if new_lines[-1][i] =="*":
            temp_sum = 1
        else:
            temp_sum=0
        for j in range(len(new_lines[:-1])):
            if new_lines[-1][i] =="*":
                temp_sum *= new_lines[j][i]
            else:
                temp_sum += new_lines[j][i]
        total_sum+=temp_sum
    """
    return total_sum


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
