import time
from pprint import pprint
from collections import defaultdict
from itertools import combinations

INPUT = "input"

with open(f"day_8/{INPUT}.txt") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

t0 = time.perf_counter()

locations = defaultdict(list)

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell != ".":
            locations[cell].append((y, x))

def find_nodes(loc_1, loc_2, p2=False):

    dy, dx = (loc_2[0] - loc_1[0], loc_2[1] - loc_1[1])
    nodes = []

    # Step backwards
    y, x = loc_1[0] - dy, loc_1[1]-dx
    if y in range(len(data)) and x in range(len(data[0])):
        nodes.append((y, x))
    if p2:
        nodes.append(loc_1)
        while y in range(len(data)) and x in range(len(data[0])):
            nodes.append((y, x))
            y -= dy
            x -= dx

    # Step forwards
    y, x = loc_2[0] + dy, loc_2[1] + dx
    if y in range(len(data)) and x in range(len(data[0])):
        nodes.append((y, x))
    if p2:
        nodes.append(loc_2)
        while y in range(len(data)) and x in range(len(data[0])):
            nodes.append((y, x))
            y += dy
            x += dx
            
    return nodes

nodes = set()
for freq in locations:
    for comb in combinations(locations[freq], 2):
        for coord in find_nodes(*comb):
           nodes.add(coord)

t1 = time.perf_counter()

print(f"Part One: {len(nodes)}, took {(t1-t0)*1000:.3f} ms")

nodes = set()
for freq in locations:
    if len(locations[freq]) > 1:
        for comb in combinations(locations[freq], 2):
            for coord in find_nodes(*comb, p2=True):
                nodes.add(coord)

t2 = time.perf_counter()
print(f"Part Two: {len(nodes)}, took {(t2-t1)*1000:.3f} ms")