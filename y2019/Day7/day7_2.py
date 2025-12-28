import itertools
import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit
filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = True

class IntComputer:
    def __init__(self, instructions, phase_value):
        self.instructions = instructions
        self.instruction_pointer = 0
        self.phase_value = phase_value

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
        if parameter:
            instruction_pointer =  self.instruction_pointer+increment
        else:
            instruction_pointer = self.instructions[self.instruction_pointer+increment]
        value = self.instructions[instruction_pointer]
        return value

    def run_computer(self, input_value):
        while True:
            opcode = str(self.instructions[self.instruction_pointer])
            instruction, first_parameter, second_parameter, third_parameter = self.decode_instruction(opcode)
            third_val, second_val, first_val = None, None, None
            if instruction in [1, 2, 5, 6, 7, 8]:
                first_val = self.decode_value(first_parameter, 1)
                second_val = self.decode_value(second_parameter, 2)
                if instruction in [1, 2, 7, 8]:
                    third_val = self.instructions[self.instruction_pointer + 3]
            match instruction:
                case 99:
                    return None
                case 3:
                    addr = self.instructions[self.instruction_pointer + 1]
                    if self.phase_value is not None:
                        self.instructions[addr] = self.phase_value
                        self.phase_value = None
                    else:
                        self.instructions[addr] = input_value
                    self.instruction_pointer += 2
                    continue
                case 4:
                    value = self.decode_value(first_parameter,1)
                    self.instruction_pointer += 2
                    return value
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


def get_my_answer():
    data = list(map(int, load_data(filepath, example=EXAMPLE).split(",")))
    possible_numbers = [5,6,7,8,9]
    all_combinations = itertools.permutations(possible_numbers, 5)
    all_outputs = []
    for combination in all_combinations:
        computers  = [IntComputer(data.copy(), combination[i]) for i in range(0,5)]
        input_value = 0
        i=0
        last_val = None
        while True:
            output = computers[i%5].run_computer(input_value)
            if output is None:
                break
            if (i % 5 == 4):
                last_val = output
            i+=1
            input_value = output
        all_outputs.append((combination, last_val))
    return max(all_outputs, key=lambda x: x[1])[1]


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="b", day=this_day, year=this_year)
