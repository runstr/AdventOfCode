import pathlib
from Tools.tools import load_data_as_lines, load_data, load_data_as_int, timeexecution
from aocd import submit

filepath = pathlib.Path(__file__).parent.resolve()
EXAMPLE = False
SUBMIT_ANSWER = False

class IntComputer:
    def __init__(self):
        self.instructions: dict = None
        self.instruction_pointer = 0
        self.relative_base = 0
        self.output=[]

    def decode_data(self, data):
        data = list(map(int, data.split(",")))
        self.instructions = {i: data[i] for i in range(len(data))}

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

    def decode_address(self, parameter, increment):
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

    def execute_command(self, instruction, first, second, address, input_value):
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
                self.instructions[address] = input_value
                self.instruction_pointer += 2
            case 4:
                self.output.append(first)
                self.instruction_pointer += 2
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

    def decode_instructions2(self):
        opcode = str(self.instructions[self.instruction_pointer])
        instruction, p1, p2, p3 = self.decode_instruction(opcode)

        first = second = address = None

        match instruction:
            case 1 | 2 | 7 | 8:
                # three parameters: value, value, address
                first = self.decode_value(p1, 1)
                second = self.decode_value(p2, 2)
                address = self.decode_address(p3, 3)

            case 3:
                # one parameter: address
                address = self.decode_address(p1, 1)

            case 4:
                # one parameter: value
                first = self.decode_value(p1, 1)

            case 5 | 6:
                # two parameters: value, value
                first = self.decode_value(p1, 1)
                second = self.decode_value(p2, 2)

            case 9:
                # one parameter: value
                first = self.decode_value(p1, 1)

            case 99:
                pass

            case _:
                raise Exception(f"Unknown opcode {instruction} at {self.instruction_pointer}")

        return instruction, first, second, address

    def decode_instructions(self):
        opcode = str(self.instructions[self.instruction_pointer])
        instruction, first_parameter, second_parameter, third_parameter = self.decode_instruction(opcode)
        first, second, address = None, None, None
        if instruction not in [3,99] :
            first = self.decode_value(first_parameter, 1)
        if instruction in [1, 2, 5, 6, 7, 8]:
            second = self.decode_value(second_parameter, 2)
        if instruction in [1, 2, 7, 8]:
            address = self.decode_address(third_parameter, 3)
        elif instruction == 3:
            address = self.decode_address(first_parameter, 1)
        return instruction, first, second, address,

    def run_computer(self):
        end_instruction = 1
        while end_instruction:
            instruction, first, second, address = self.decode_instructions2()
            end_instruction = self.execute_command(instruction, first, second, address, 1)


def get_my_answer():
    data = load_data(filepath, example=EXAMPLE)
    computer = IntComputer()
    computer.decode_data(data)
    computer.run_computer()
    return computer.output[0]


@timeexecution
def execution():
    submit_answer = SUBMIT_ANSWER
    my_answer = get_my_answer()
    print(my_answer)
    this_day = int(str(filepath).split("\\")[-1][3:])
    this_year = int(str(filepath).split("\\")[-2][1:])
    if submit_answer:
        submit(my_answer, part="a", day=this_day, year=this_year)
