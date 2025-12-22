from datetime import date
from aocd import get_data
from os import path, environ
import subprocess
import time
import sys
import os


def set_cookie():
    with open("../private.env", "r") as f:
        data = f.read()
        environ["AOC_SESSION"] = data.split("=")[1]


def load_data(filepath, example=False):
    if example:
        filepath = str(filepath)+"\\example.txt"
    else:
        filepath = str(filepath)+"\\input.txt"
    with open(filepath, "r") as f:
        data = f.read()
    return data


def load_data_as_lines(filepath, example=False):
    if example:
        filepath = str(filepath)+"\\example.txt"
    else:
        filepath = str(filepath)+"\\input.txt"
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    return data


def load_data_as_map(filepath, example=False):
    if example:
        filepath = str(filepath)+"\\example.txt"
    else:
        filepath = str(filepath)+"\\input.txt"
    with open(filepath, "r") as f:
        data = f.read().splitlines()
    mapping = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            mapping[(x,y)] = data[y][x]
    max_y, max_x = len(data), len(data[0])
    return mapping, max_x,  max_y

def load_data_as_int(filepath, example=False):
    if example:
        filepath = str(filepath)+"\\example.txt"
    else:
        filepath = str(filepath)+"\\input.txt"
    input_full = []
    with open(filepath, "r") as f:
        for input_line in f.read().splitlines():
            input_line_list = []
            for i in input_line:
                input_line_list.append(int(i))
            input_full.append(input_line_list)
    return input_full

def load_data_as_chars(filepath, example=False):
    if example:
        filepath = str(filepath)+"\\example.txt"
    else:
        filepath = str(filepath)+"\\input.txt"
    input_full = []
    with open(filepath, "r") as f:
        for input_line in f.read().splitlines():
            input_line_list = []
            for i in input_line:
                input_line_list.append(i)
            input_full.append(input_line_list)
    return input_full

def get_todays_date():
    return str(date.today().day)


def insert_data(todays_date, year):
    day_name = __file__[:-14]+"y"+str(year)+"\\Day"+todays_date

    if not path.exists(day_name):
        bat_file = "new_day.bat"
        working_dir = r"C:\Users\Rune\AdventOfCode\Tools"
        subprocess.run([bat_file, str(todays_date), str(year)], cwd=working_dir, shell=True)
        # Re-execute the current Python script
        python = sys.executable  # path to the Python interpreter
        os.execv(python, [python] + sys.argv)

    filename = __file__[:-14]+"y"+str(year)+"\\Day"+todays_date+"\\input.txt"
    if path.isfile(filename) or path.getsize(filename) == 0:
        with open(filename, "w") as inputfile:
            inputfile.write(get_data(year=year, day=int(todays_date)))


def timeexecution(function):
    def timed(*args, **kw):
        ts = time.time()
        result = function(*args, **kw)
        te = time.time()
        print("Time taken = {}".format(te-ts))
        return result
    return timed
