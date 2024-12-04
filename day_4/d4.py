import time
import copy

import numpy as np

INPUT = "input"

with open(f"day_4/{INPUT}.txt") as f:
    data = np.array([list(s) for s in f.read().splitlines()])
                    

def search_data(data: list):
  temp_counter = 0
  for line in data:
      temp_counter += "".join(line).count("XMAS")
      temp_counter += "".join(line).count("SAMX")
  return temp_counter

def get_diagonals(arr:np.ndarray):
    diag_forward: list[str] = ["".join(arr.diagonal(offset).tolist()) for offset in range(-arr.shape[0] + 1, arr.shape[1])]

    flipped_arr: np.ndarray = np.fliplr(arr)
    diag_backward: list[str] = ["".join(flipped_arr.diagonal(offset).tolist()) for offset in range(-flipped_arr.shape[0] + 1, flipped_arr.shape[1])]

    return diag_forward, diag_backward

t0 = time.perf_counter()

p1 = 0
p1 += search_data(data)
p1 += search_data(data.T)

diag_forward, diag_backward = get_diagonals(data)

p1 += search_data(diag_forward)
p1 += search_data(diag_backward)

t1 = time.perf_counter()

print(f"Part One: {p1}, took {(t1-t0)*1000:.3f} ms")

def get_neighbours(data, x, y) -> tuple:
    return (str(data[y-1][x-1]), str(data[y+1][x+1])), (str(data[y-1][x+1]), str(data[y+1][x-1]))

def find_xmas(data, x, y, print_valid=False):
    neighbours = get_neighbours(data, x, y)
    if all ("".join(neighbour) in ("MS", "SM") for neighbour in neighbours):
        if print_valid:
            demo_list = copy.deepcopy([row[x-1:x+2].tolist() for row in data[y-1:y+2]])
            for dy, dx in ((0, 1), (1, 0), (1, 2), (2, 1)):
                # continue
                demo_list[dy][dx] = " "
                # print("")
                # for line in demo_list:
                #     print("".join(line))
            pass
        return 1
    return 0

p2 = 0
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "A":
            try:
                p2 += find_xmas(data, x, y, print_valid=True)
            except IndexError:
                continue

t2 = time.perf_counter()

print(f"Part Two: {p2}, took {(t2-t1)*1000:.3f} ms")