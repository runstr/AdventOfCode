import pathlib
import random

from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

class IntComputer:
    def __init__(self, instructions, phase_value):
        self.instructions: dict = instructions
        self.instruction_pointer = 0
        self.phase_value = phase_value
        self.relative_base = 0
        self.output=[]
        self.score = 0
        self.walls = set()
        self.ball = None
        self.paddle = None
        self.empty = set()
        self.blocks = set()
        self.block_value =2
        self.empty_value = 0
        self.wall_value = 1
        self.ball_value = 4
        self.paddle_value = 3

    def decode_instruction(self, opcode):
        """
        Decode an opcode instruction
        :param opcode:
        :return:
        """
        opcode = "0" * (5 - len(opcode)) + opcode
        instruction = int(opcode[-2:])
        first, second, third = int(opcode[-3]), int(opcode[-4]), int(opcode[-5])
        return instruction, first, second, third

    def decode_value(self, parameter, increment):
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
        value = self.instructions[instruction_pointer]
        return value

    def decode_write(self, parameter, increment):
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
        return instruction_pointer

    def run_computer(self):
        while True:
            opcode = str(self.instructions[self.instruction_pointer])
            instruction, first_parameter, second_parameter, third_parameter = self.decode_instruction(opcode)
            third_val, second_val, first_val = None, None, None
            if instruction in [1, 2, 3, 5, 6, 7, 8, 9]:
                first_val = self.decode_value(first_parameter, 1)
                if instruction in [1, 2, 3, 5, 6, 7, 8]:
                    second_val = self.decode_value(second_parameter, 2)
                if instruction in [1, 2, 7, 8]:
                    third_val = self.decode_write(third_parameter, 3)
            match instruction:
                case 99:
                    return None
                case 3:
                    addr = self.decode_write(first_parameter, 1)
                    input_value = self.move_joystick()
                    if self.phase_value is not None:
                        self.instructions[addr] = self.phase_value
                        self.phase_value = None
                    else:
                        self.instructions[addr] = input_value
                    self.instruction_pointer += 2
                    continue
                case 4:
                    value = self.decode_value(first_parameter,1)
                    self.output.append(value)
                    if len(self.output) ==3:
                        if self.output[0] == -1 and self.output[1] == 0 and not self.blocks:
                            return self.output[2]
                        self.decode_output()
                        self.output = []

                    self.instruction_pointer += 2
                    continue
                case 1:
                    self.instructions[third_val] = first_val + second_val
                    self.instruction_pointer += 4
                case 2:
                    self.instructions[third_val] = first_val * second_val
                    self.instruction_pointer += 4
                case 5:
                    if first_val:
                        self.instruction_pointer = second_val
                    else:
                        self.instruction_pointer += 3
                case 6:
                    if not first_val:
                        self.instruction_pointer = second_val
                    else:
                        self.instruction_pointer += 3
                case 7:
                    self.instructions[third_val] = int(first_val < second_val)
                    self.instruction_pointer += 4
                case 8:
                    self.instructions[third_val] = int(first_val == second_val)
                    self.instruction_pointer += 4
                case 9:
                    self.relative_base += first_val
                    self.instruction_pointer += 2

    def decode_output(self):
        x, y, op = self.output[0], self.output[1], self.output[2]
        if op == self.paddle_value:
            self.paddle = (x, y)
        elif op == self.empty_value:
            if (x,y) in self.blocks:
                self.blocks.remove((x, y))
            self.empty.add((x,y))
        elif op == self.wall_value:
            self.walls.add((x,y))
        elif op == self.ball_value:
            self.ball = (x,y)
        elif op == self.block_value:
            self.blocks.add((x,y))
        elif x ==-1 and y ==0:
            self.score = op

    def move_joystick(self):
        ball_x = self.ball[0]
        joystick_x = self.paddle[0]
        if ball_x>joystick_x:
            return 1
        if ball_x<joystick_x:
            return -1
        return 0



def get_my_answer():
    data = list(map(int,load_data(filepath, example=EXAMPLE).split(",")))
    data_dict = {i:data[i] for i in range(len(data))}
    data_dict[0] = 2
    computer = IntComputer(data_dict, None)
    return computer.run_computer()

@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
