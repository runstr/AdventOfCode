import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def get_my_answer():
    lines = load_data_as_lines(filepath, example=EXAMPLE)
    data = {}
    for line in lines:
        fuels, product = line.split(" => ")
        product_amount, prod_type = product.split(" ")
        fuels = fuels.split(", ")
        a=[int(product_amount)]
        for fuel in fuels:
            amount, typ = fuel.split(" ")
            a.append((int(amount),typ))
        data[prod_type] = a
    fuels = [("FUEL", 1)]
    while fuels:
        fuel, val = fuels.pop()
        next_fuels= data[fuel]
        amount = next_fuels[0]
        for fuel in next_fuels[1:]:
            print(fuel, amount)
    return data


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
