from day_imports import *

if __name__ == '__main__':
    set_cookie()
    for i in range(23, 24):
        print("-"*30)
        todays_date = str(i)
        insert_data(todays_date, 2020)
        print(f"Running day {i} part A")
        exec("day{}_1.execution()".format(todays_date))

        print(f"\nRunning day {i} part B")
        exec("day{}_2.execution()".format(todays_date))
        print("-" * 30)
        print("\n")
