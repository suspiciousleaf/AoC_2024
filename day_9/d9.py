import time
from collections import deque

INPUT = "input"

with open(f"day_9/{INPUT}.txt") as f:
    data = [int(num) for num in f.read()]

t0 = time.perf_counter()


def find_last_file(data: list):
    last_char = data.pop()
    if last_char == ".":
        last_char = find_last_file(data)
    return last_char


def create_data(data):
    full_data = []
    id = 0
    for lp, num in enumerate(data):
        if not lp % 2:
            for j in range(num):
                full_data.append(str(id))
            id += 1
        else:
            if num:
                for j in range(num):
                    full_data.append(".")
    return full_data


data = create_data(data)

def get_checksum(data):
    checksum = 0
    for i, num in enumerate(data):
        if num.isdigit():
            checksum += i * int(num)
    return checksum

def part_one(data):
    for i, char in enumerate(data):
        try:
            if char == ".":
                last_file_slice = find_last_file(data)
                data[i] = last_file_slice
        except IndexError:
            pass
    return get_checksum(data)



t1 = time.perf_counter()
print(f"Part One: {part_one(data.copy())}, took {(t1-t0)*1000:.3f} ms")

def find_empty_slots(data):
    # This will hold the locations of every empty slot, with key as the length of the slot, in order of appearance, index of the first tile of that slot

    lp = 0
    empty_locations = {i:deque() for i in range(1, 10)}

    while lp < len(data):
        if data[lp] == ".":
            temp_list = deque(maxlen=9)
            rp = lp
            while data[rp] == ".":
                temp_list.append(data[rp])
                rp += 1
            empty_locations[len(temp_list)].append(lp)
            lp += len(temp_list) - 1
        lp +=1
    return empty_locations


def part_two(data):
    empty_locations: list[deque] = find_empty_slots(data)
    i = len(data) - 1
    lp, rp = i, i

    while rp >= 0:
        if data[rp] != ".":
            temp_list = deque(maxlen=9)
            lp = rp
            while data[lp] == data[rp]:
                temp_list.append(data[lp])
                lp -= 1
                if lp == -1:
                    break
            rp -= len(temp_list) - 1
            chunk_size = len(temp_list)
            lowest_index = rp
            slot_size = 0
            for slot in [slots for slots in empty_locations if slots >= chunk_size and empty_locations[slots]]:
                if empty_locations[slot][0] < lowest_index:
                    lowest_index = empty_locations[slot][0]
                    slot_size = slot
            if lowest_index != rp:
                data[lowest_index:lowest_index+chunk_size] = temp_list
                data[lp+1:lp+chunk_size+1] = ["." for _ in range(chunk_size)]
                used_slot = empty_locations[slot_size].popleft()
                remaining_empty_slot = slot_size - chunk_size
                if remaining_empty_slot:
                    empty_locations[remaining_empty_slot].append(used_slot + chunk_size)
                    empty_locations[remaining_empty_slot] = deque(sorted(empty_locations[remaining_empty_slot]))

        rp -= 1
    return get_checksum(data)


t2 = time.perf_counter()
print(f"Part Two: {part_two(data.copy())}, took {(t2 - t1)*1000:.3f} ms")
