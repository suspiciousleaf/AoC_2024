import time
INPUT = "input"

with open(f"day_1/{INPUT}.txt", "r") as f:
  data = [[int(num) for num in line.strip().split(" ") if num] for line in f.readlines()]
t0 = time.perf_counter()

list_1 = sorted([line[0] for line in data])
list_2 = sorted([line[1] for line in data])

diff = 0

for num_1, num_2 in zip(list_1, list_2):
   diff += abs(num_1 - num_2)

t1 = time.perf_counter()
print(f"Part One: {diff}, took {(t1 - t0)*1000:.3f} ms")


total = 0
for num in list_1:
   total += (num * list_2.count(num))

print(f"Part Two: {total}, took {(time.perf_counter() - t1)*1000:.3f} ms")