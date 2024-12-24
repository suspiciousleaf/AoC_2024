import time

INPUT = "input"

t0 = time.perf_counter()


def extract_coords(line):
    field_mapping = {"A": 3, "B": 1}
    temp_coords = [field_mapping.get(line[7], 0)]
    for coord in line.split(","):
        temp_coords.append(int("".join([digit for digit in coord if digit.isdigit()])))
    return tuple(temp_coords)


with open(f"day_13/{INPUT}.txt") as f:
    data = []
    for machine in f.read().split("\n\n"):
        machine_data = []
        for line in machine.split("\n"):
            machine_data.append(extract_coords(line))
        data.append(machine_data)


def validate_combination(combination, target):
    x = sum([press[1] for press in combination])
    y = sum([press[2] for press in combination])
    return (x, y) == target[1:]


max_repeats = 100
total_tokens = 0
for machine in data:
    valid = False
    for count0 in range(max_repeats + 1):
        for count1 in range(max_repeats + 1):
            if not valid:
                combination = [machine[0]] * count0 + [machine[1]] * count1
                if validate_combination(combination, machine[2]):
                    valid = True
                    total_tokens += sum([press[0] for press in combination])
                    print(f"{total_tokens=}")

t1 = time.perf_counter()
print(f"Part One: {total_tokens}, took {t1 - t0:.3f} s")
