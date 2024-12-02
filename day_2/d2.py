import time

t0 = time.perf_counter()

INPUT = "input"

data = []
with open(f"day_2/{INPUT}.txt", "r") as f:
    data = [[int(num) for num in line.split(" ")] for line in f]

def increase_record(record):
    for i, num in enumerate(record[:-1]):
        if num < record[i+1] <= num + 3:
            continue
        else:
            return False
    return True

def decrease_record(record):
    for i, num in enumerate(record[:-1]):
        if num > record[i+1] >= num - 3:
            continue
        else:
            return False
    return True

def filter_direction(record):
    if record[1] > record[0]:
        return increase_record(record)
    return decrease_record(record)

valid_logs = 0
for record in data:
    if filter_direction(record):
        valid_logs += 1


t1 = time.perf_counter()        
print(f"Part One: {valid_logs}, took {(t1 - t0) * 1000:.3f} ms")


def damper(record):
    if filter_direction(record): 
        return True
    else:
        for i, _ in enumerate(record):
            temp = record.copy()
            temp.pop(i)
            if filter_direction(temp):
                return True
    return False


valid_logs_two = 0
for record in data:
    if damper(record):
        valid_logs_two += 1

t2 = time.perf_counter()

print(f"Part Two: {valid_logs_two}, took {(t2 - t1) * 1000:.3f} ms")
