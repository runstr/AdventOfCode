import math
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

class Moons:
    def __init__(self, data):
        self.data = data
        self.positions = None
        self.velocities = None
        self.previous = [set(), set(), set()]

    def initialize_moons(self):
        self.positions = []
        self.velocities = []
        for line in self.data:
            x, y, z = line[1:-1].split(", ")
            self.positions.append([int(x[2:]), int(y[2:]), int(z[2:])])
            self.velocities.append([0, 0, 0])

    def apply_gravity(self,):
        for i in range(len(self.positions)):
            for j in range(len(self.positions)):
                if j == i:
                    continue
                for k in range(3):
                    if self.positions[i][k] > self.positions[j][k]:
                        self.velocities[i][k] -= 1
                    elif self.positions[i][k] < self.positions[j][k]:
                        self.velocities[i][k] += 1

    def apply_velocity(self):
        for i in range(len(self.positions)):
            for j in range(3):
                self.positions[i][j] += self.velocities[i][j]

    def get_energies(self):
        total_energy = 0
        for i in range(len(self.positions)):
            pos = self.positions[i]
            vel = self.velocities[i]
            pos_energy = abs(pos[0]) + abs(pos[1]) +abs(pos[2])
            kin_energy = abs(vel[0]) + abs(vel[1]) + abs(vel[2])
            total_energy +=pos_energy *kin_energy
        return total_energy

    def compare_previous(self, this_value, k):
        if this_value in self.previous[k]:
            return True
        else:
            self.previous[k].add(this_value)
            return False

def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    moons = Moons(data)
    moons.initialize_moons()
    previous_points = [-1, -1, -1]
    for i in range(10000000):
        for j in range(3):
            this_value = (moons.positions[0][j], moons.positions[1][j], moons.positions[2][j], moons.positions[3][j],
                          moons.velocities[0][j], moons.velocities[1][j], moons.velocities[2][j], moons.velocities[3][j])
            if moons.compare_previous(this_value, j):
                if previous_points[j] == -1:
                    previous_points[j] =i
        if -1 not in previous_points:
            break
        moons.apply_gravity()
        moons.apply_velocity()

    return math.lcm(previous_points[0], previous_points[1], previous_points[2])


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
