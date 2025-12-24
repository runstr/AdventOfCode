import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = True
SUBMIT_ANSWER = False

def get_my_answer():
    player1, player2 = load_data(filepath, example=EXAMPLE).split("\n\n")
    player1 = list(map(int,player1.split("\n")[1:]))
    player2 = list(map(int,player2.split("\n")[1:]))
    i=0
    player1_decs = set()
    player2_decs = set()
    """
    while True:
        p1, p2 = player1.pop(0), player2.pop(0)
        if p1 > p2:
            player1+=[p1,p2]
        elif p1 < p2:
            player2+=[p2,p1]
        else:
            player1+=[p1,p2]
        player1_dec = ",".join(list(map(str,player1)))
        player2_dec = ",".join(list(map(str,player2)))
        if player1_dec in player1_decs:
            break
        if player2_dec in player2_decs:
            break
    """



@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
