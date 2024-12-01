import time
from collections import Counter

t0 = time.perf_counter()

INPUT = "input"

# Using slice objects is more verbose, and roughly the same speed as using .split("   ")
if INPUT == "example":
   num_1 = slice(0, 1)
   num_2 = slice(4, 5)
elif INPUT == "input":
   num_1 = slice(0, 5)
   num_2 = slice(8, 13)
else:
   raise Exception("Unrecognized input file")

list_1, list_2 = [], []

# .read().splitlines() proved to be slightly faster (0.02 ms) than .splitlines() or looping over f, which surprised me
with open(f"day_1/{INPUT}.txt", "r") as f:
   for line in f.read().splitlines():
      list_1.append(int(line[num_1]))
      list_2.append(int(line[num_2]))

list_1.sort()
list_2.sort()

diff = 0

for num_1, num_2 in zip(list_1, list_2):
   diff += abs(num_1 - num_2)

t1 = time.perf_counter()
print(f"Part One: {diff}, took {(t1 - t0) * 1000:.3f} ms")

# Using a Counter object over .count() improves speed by ~20x
my_counter = Counter(list_2)

total = 0
for num in list_1:
   # Here, avoiding 0 multiplication saves ~0.4 ms, even with the additional assignment to "frequency" variable
   frequency = my_counter[num]
   if frequency:
      total += (num * frequency) 

print(f"Part Two: {total}, took {(time.perf_counter() - t1) * 1000:.3f} ms")