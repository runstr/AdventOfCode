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






def get_my_answer():
    data = load_data_as_lines(filepath, example=EXAMPLE)
    moons = Moons(data)
    moons.initialize_moons()
    for i in range(1000):
        moons.apply_gravity()
        moons.apply_velocity()
    return moons.get_energies()


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
