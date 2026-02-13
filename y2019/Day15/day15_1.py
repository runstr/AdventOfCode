import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

class IntComputer:
    def __init__(self):
        self.instructions: dict = None
        self.instruction_pointer: int = 0
        self.relative_base: int = 0
        self.output: list =[]
        self.input_value = 1

    def decode_data(self, data):
        data = list(map(int, data.split(",")))
        self.instructions = {i: data[i] for i in range(len(data))}

    def decode_opcode(self, opcode):
        """
        Decode an opcode instruction
        :param opcode:
        :return:
        """
        opcode = "0" * (5 - len(opcode)) + opcode
        instruction = int(opcode[-2:])
        first, second, third = int(opcode[-3]), int(opcode[-4]), int(opcode[-5])
        return instruction, first, second, third

    def decode_value(self, parameter: int , increment: int):
        if parameter == 1:
            instruction_pointer =  self.instruction_pointer+increment
        elif parameter == 0:
            instruction_pointer = self.instructions[self.instruction_pointer+increment]
        elif parameter == 2:
            instruction_pointer = self.instructions[self.instruction_pointer + increment] + self.relative_base
        else:
            raise Exception(f"Invalid parameter: {parameter}")
        if instruction_pointer not in self.instructions:
            self.instructions[instruction_pointer] = 0
        return self.instructions[instruction_pointer]

    def decode_address(self, parameter: int, increment: int):
        if parameter == 1:
            raise Exception(f"Invalid parameter: {parameter}")
        elif parameter == 0:
            instruction_pointer = self.instructions[self.instruction_pointer+increment]
        elif parameter == 2:
            instruction_pointer = self.instructions[self.instruction_pointer + increment] + self.relative_base
        else:
            raise Exception(f"Invalid parameter: {parameter}")
        if instruction_pointer not in self.instructions:
            self.instructions[instruction_pointer] = 0
        return instruction_pointer

    def execute_command(self):
        instruction, first, second, address = self.decode_instructions()
        match instruction:
            case 99:
                return 0
            case 1:
                self.instructions[address] = first + second
                self.instruction_pointer += 4
            case 2:
                self.instructions[address] = first * second
                self.instruction_pointer += 4
            case 3:
                self.instructions[address] = self.input_value
                self.instruction_pointer += 2
            case 4:
                self.output.append(first)
                self.instruction_pointer += 2
                return -1
            case 5:
                if first:
                    self.instruction_pointer = second
                else:
                    self.instruction_pointer += 3
            case 6:
                if not first:
                    self.instruction_pointer = second
                else:
                    self.instruction_pointer += 3
            case 7:
                self.instructions[address] = int(first < second)
                self.instruction_pointer += 4
            case 8:
                self.instructions[address] = int(first == second)
                self.instruction_pointer += 4
            case 9:
                self.relative_base += first
                self.instruction_pointer += 2
        return 1

    def decode_input(self):
        return 3

    def decode_instructions(self):
        opcode = str(self.instructions[self.instruction_pointer])
        instruction, p1, p2, p3 = self.decode_opcode(opcode)
        first = second = address = -1
        if instruction == 99:
            return instruction, first, second, address,
        if instruction == 3:
            address = self.decode_address(p1, 1)
            return instruction, first, second, address,
        first = self.decode_value(p1, 1)
        second = self.decode_value(p2, 2)
        if instruction in [1,2,7,8]:
            address = self.decode_address(p3, 3)
            return instruction, first, second, address,

        return instruction, first, second, address,

    def run_computer(self):
        end_instruction = 1
        directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
        keys = [1,2,3,4]
        visited = {}
        next_paths = [((0,0), 0, self.instructions.copy(),0)]
        possible_paths = []
        while next_paths:
            this_path = next_paths.pop()
            data = this_path[2]
            this_point = this_path[0]
            steps = this_path[1]
            inst_pointer = this_path[3]
            for key in keys:
                new_point = (this_point[0]+directions[key][0], this_point[1]+directions[key][1])
                new_steps= steps+1
                if new_point in visited and new_steps > visited[new_point]:
                    continue
                self.instructions = data
                self.instruction_pointer = inst_pointer
                self.input_value = key

                while end_instruction:
                    end_instruction = self.execute_command()
                    if end_instruction == -1:
                        output = self.output[0]
                        self.output = []
                        break
                visited[new_point] = new_steps
                if output == 2:
                    possible_paths.append(new_point)
                elif output ==1:
                    next_paths.append((new_point, new_steps, self.instructions.copy(), self.instruction_pointer))
                else:
                    continue
        return possible_paths



def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    computer = IntComputer()
    computer.decode_data(data)
    return computer.run_computer()


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
