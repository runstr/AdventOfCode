import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False
import re

def check_valid(rule, passport):
    match rule:
        case "byr:":
            # Regex rule. Search for all occurences that
            # 1. starts with byr:
            # 2. follows with numbers with number between 1920 and 1999 (19[2-9][0-9]) OR 2000-2002)
            # 3. looks ahead ?= to see if next char are either end of string ($) or escape sequence \s (new line, space etc)
            regex_rule = r"byr:(19[2-9][0-9]|200[0-2])(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "iyr:":
            # Similar rule to above
            regex_rule = r"iyr:(201[0-9]|2020)(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "eyr:":
            # Similar rule to above
            regex_rule = r"eyr:(202[0-9]|2030)(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "hgt:":
            # Similar rule to above, but some numbers has to end with cm and some has to end with in
            regex_rule = r"hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "hcl:":
            # Regex rule. Search for all occurences that
            # 1. starts with hcl:#
            # 2. Follows with exactly 6 characters {6} that are hexadecimal (ether 0 to 9 or a-f)
            # 3. looks ahead ?= to see if next char are either end of string ($) or escape sequence \s (new line, space etc)
            regex_rule = r"hcl:#([0-9a-f]){6}(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "ecl:":
            # Regex rule. Search for all occurences that
            # 1. starts with ecl:
            # 2. Follows with exactly one of the strings after this
            # 3. looks ahead ?= to see if next char are either end of string ($) or escape sequence \s (new line, space etc)

            regex_rule = r"ecl:(amb|blu|brn|gry|grn|hzl|oth)(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "pid:":
            # Regex rule. Search for all occurences that
            # 1. starts with pid:
            # 2. Follows with exactly 9 digits that are  0 to 9
            # 3. looks ahead ?= to see if next char are either end of string ($) or escape sequence \s (new line, space etc)
            regex_rule = r"pid:([0-9]){9}(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
        case "cid:":
            # Regex rule. Search for all occurences that
            # 1. starts with cid:
            # 2. Follows with all characters until 3.
            # 3. looks ahead ?= to see if next char are either end of string ($) or escape sequence \s (new line, space etc)

            regex_rule = r"cid:[\w]+(?=$|\s)"
            value = re.search(regex_rule, passport)
            value = value.group() if value else None
            # Since CID is don't care return true anyways. Only here for learning
            return True
    return bool (value)

def get_my_answer():
    data = load_data(filepath, example=EXAMPLE).split("\n\n")
    rules = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:", "cid:"]
    count = 0
    for passport in data:
        valid = True
        for rule in rules:
            valid = check_valid(rule, passport)
            if not valid:
                break
        if valid:
            count += 1

    return count


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
