import time

INPUT = "input"

with open(f"day_9/{INPUT}.txt") as f:
    data = [int(num) for num in f.read()]

t0 = time.perf_counter()

full_data = []

id = 0
for i, num in enumerate(data):
    if not i % 2:
        for j in range(num):
            full_data.append(str(id))
        id += 1
    else:
        if num:
            for j in range(num):
                full_data.append(".")

def find_last_file(full_data: list):
    last_char = full_data.pop()
    if last_char == ".":
        last_char = find_last_file(full_data)
    return last_char


for i, char in enumerate(full_data):
    try:
        if char == ".":
            last_file_slice = find_last_file(full_data)
            full_data[i] = last_file_slice
    except IndexError:
        pass



# print("".join(full_data))

def get_checksum(full_data):
    checksum = 0
    for i, num in enumerate(full_data):
        checksum += i * int(num)
    return checksum

t1 = time.perf_counter()
print(f"Part One: {get_checksum(full_data)}, took {(t1-t0)*1000:.3f} ms")
