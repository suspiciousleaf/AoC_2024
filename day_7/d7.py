import time
from itertools import product
import math

INPUT = "input"

with open(f"day_7/{INPUT}.txt") as f:
    data = {int(key): [int(num) for num in value.split(" ")] for key, value in (line.split(": ") for line in f.read().splitlines())}

t0 = time.perf_counter()

def precompute_shifts(value:list[int]) -> list[int]:
    return [10**(math.floor(math.log10(num)) + 1) for num in value[1:]]

def find_valid(key: int, value:list[int], options:list[str]) -> int | None:
    shifts = precompute_shifts(value)
    for option in options:
        running_total = value[0]
        for op, num, shift in zip(option, value[1:], shifts):
            if op == "+":
                running_total += num
            elif op == "*":
                running_total *= num
            elif op == "||":
                running_total *= shift
                running_total += num
            if running_total > key:
                break 
        if running_total == key:
            return key

def compute(data: dict, operands: list) -> int:
    total = 0
    options = {i:list(product(operands, repeat=i)) for i in range(max([len(value) for value in data.values()]))}
    for key, value in data.items():
        valid = find_valid(key, value, options[len(value)-1])
        if valid:
            total += valid
    return total

p1: int = compute(data, ["+", "*"])
t1: float = time.perf_counter()
print(f"Part One: {p1}, took {(t1-t0)*1000:.3f} ms")

p2: int = compute(data, ["+", "*", "||"])
t2: float = time.perf_counter()
print(f"Part Two: {p2}, took {(t2-t1):.3f} s")



    