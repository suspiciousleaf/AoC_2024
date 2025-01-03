import time


INPUT = "input"

with open(f"day_17/{INPUT}.txt") as f:
    data = f.read().split("\n\n")


def get_combo_operand(op):
    global A, B, C
    if 0 <= op <= 3:
        return op
    match op:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            raise ValueError("Invalid program")


def adv(operand):
    """The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register."""
    global A, debug
    if debug:
        print(
            f"adv called, register A changed from {A} to {A // 2 ** get_combo_operand(operand)}"
        )
    A = A // 2 ** get_combo_operand(operand)


def bxl(operand):
    """The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B."""
    global B, debug
    if debug:
        print(f"bxl called, register B changed from {B} to {B ^ operand}")
    B = B ^ operand


def bst(operand):
    """The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register."""
    global B, debug
    if debug:
        print(
            f"bst called, register B changed from {B} to {get_combo_operand(operand) % 8}"
        )
    B = get_combo_operand(operand) % 8


def jnz(operand):
    """The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction."""
    global pointer, debug
    if A == 0:
        if debug:
            print("jnz called with A = 0, pointer value unchanged")
    else:
        if debug:
            print(f"jnz called with A > 0, pointer value set to {operand}")
        pointer = operand - 2


def bxc(operand):
    """The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)"""
    global B, C, debug
    if debug:
        print(f"bxc called, register B changed from {B} to {B ^ C}")
    B = B ^ C


def out(operand):
    """The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)"""
    global debug
    if debug:
        print(f"out called, appended {get_combo_operand(operand) % 8} to output log")
    output.append(str(get_combo_operand(operand) % 8))


def bdv(operand):
    """The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)"""
    global A, B, debug
    if debug:
        print(
            f"bdv called, register B changed from {B} to {A // 2 ** get_combo_operand(operand)}"
        )
    B = A // 2 ** get_combo_operand(operand)


def cdv(operand):
    """The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)"""
    global A, C, debug
    if debug:
        print(
            f"cdv called, register C changed from {C} to {A // 2 ** get_combo_operand(operand)}"
        )
    C = A // 2 ** get_combo_operand(operand)


opcode_mapping = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

t0 = time.perf_counter()

program_data = [int(num) for num in data[1].replace("Program: ", "").split(",")]

A, B, C = [int(num.split(":")[1]) for num in data[0].split("\n")]

pointer = 0
output = []
debug = False

while pointer < len(program_data):
    opcode, operand = program_data[pointer : pointer + 2]
    opcode_mapping[opcode](operand)
    pointer += 2

print(f"Output: {",".join(output)}, took {(time.perf_counter() - t0)*1000:.3f} ms")
