import time
import numpy as np

INPUT = "input"

t0 = time.perf_counter()


def extract_coords(line):
    temp_coords = []
    for coord in line.split(","):
        temp_coords.append(int("".join([digit for digit in coord if digit.isdigit()])))
    return temp_coords


with open(f"day_13/{INPUT}.txt") as f:
    data = []
    for machine in f.read().split("\n\n"):
        tmp = []
        for line in machine.split("\n"):
            tmp.append(extract_coords(line))
        machine_data = {
            "coefficients": np.array([[tmp[0][0], tmp[1][0]], [tmp[0][1], tmp[1][1]]]),
            "constants": np.array(tmp[2]),
        }
        data.append(machine_data)


def confirm_integer(solution):
    return all(abs(num - round(num)) < 0.0001 and round(num) >= 0 for num in solution)


def find_solutions(data, pt1: bool = True):
    x, y = 0, 0
    for machine in data:
        solution = np.linalg.solve(machine["coefficients"], machine["constants"])
        if not confirm_integer(solution) or (pt1 and any(z > 100 for z in solution)):
            continue
        x += solution[0]
        y += solution[1]

    return x, y


x, y = find_solutions(data, pt1=True)
total_tokens = int((x * 3) + y)
t1 = time.perf_counter()
print(f"Part One: {total_tokens}, took {(t1 - t0)*1000:.3f} ms")

INCREASE = 10000000000000

for machine in data:
    machine["constants"][0] += INCREASE
    machine["constants"][1] += INCREASE


x, y = find_solutions(data, pt1=False)
total_tokens = int((x * 3) + y)
t2 = time.perf_counter()
print(f"Part Two: {total_tokens}, took {(t2 - t1)*1000:.3f} ms")
