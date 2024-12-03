import re
import time

INPUT = "input"

with open(f"day_3/{INPUT}.txt", "r") as f:
    data = f.read()

t0 = time.perf_counter()

def mul(section):
    sum = 0
    matches = re.findall(pattern="mul\(\d{1,3},\d{1,3}\)", string=section)
    for match in matches:
        a, b = match.split(",")
        a = int("".join([num for num in a if num.isdigit()]))
        b = int("".join([num for num in b if num.isdigit()]))
        sum += a * b

    return sum

    
p1 = mul(data)
t1 = time.perf_counter()
print(f"Part One: {p1}, took {(t1-t0)*1000:.3f} ms")

enabled_sections = []
disabled_sections = re.split("don't\(\)", data)
enabled_sections.append(disabled_sections.pop(0))
for section in disabled_sections.copy():
    split_sections = re.split("do\(\)", section)
    disabled_sections.append(split_sections.pop(0))
    enabled_sections.extend(split_sections)

p2 = 0

for section in enabled_sections:
    p2 += mul(section)

t2 = time.perf_counter()

print(f"Part Two: {p2}, took {(t2-t1)*1000:.3f} ms")
