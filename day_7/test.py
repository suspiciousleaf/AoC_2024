from collections import deque
from typing import List, Tuple
import time
 
 
def read_file(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        return f.read()
 
 
def parse_input(advent_input: str) -> List[Tuple[int, List[int]]]:
    lines = advent_input.strip().split("\n")
    return [
        (int(line.split(":")[0]), [int(x) for x in line.split(":")[1].strip().split()])
        for line in lines
    ]
 
 
def remove_matching_digits(num1: int, num2: int) -> int:
    num1_str, num2_str = str(num1), str(num2)
 
    if num1_str.endswith(num2_str):
        result_num1_str = num1_str[: -len(num2_str)]
        return int(result_num1_str) if result_num1_str else 0
 
    return None
 
 
# is_part2 eshte katastrofal po spo kodoj per pare
def can_be_built(target: int, input_values: List[int], is_part2: bool) -> bool:
    visited = set()
    queue = deque([(target, 0)])
    reversed_input = list(reversed(input_values))
    while queue:
        left = queue.popleft()
        (entry, depth) = left
        if entry == 0:
            return True
        if (
            left in visited
            or entry < 0
            or entry > target
            or depth >= len(reversed_input)
        ):
            continue
        visited.add(left)
        queue.append((entry - reversed_input[depth], depth + 1))
        if entry % reversed_input[depth] == 0:
            queue.append((int(entry / reversed_input[depth]), depth + 1))
        if is_part2:
            removed_value = remove_matching_digits(entry, reversed_input[depth])
            if removed_value is not None:
                queue.append((removed_value, depth + 1))
    return False
 
 
def part1(parsed_input: List[Tuple[int, List[int]]]):
    sum_built = 0
    for current_target, input_value in parsed_input:
        if can_be_built(current_target, input_value, False):
            sum_built += current_target
    print(sum_built)
 
 
def part2(parsed_input: List[Tuple[int, List[int]]]):
    sum_built = 0
    for current_target, input_value in parsed_input:
        if can_be_built(current_target, input_value, True):
            sum_built += current_target
    print(sum_built)
 
 
if __name__ == "__main__":
    t0 = time.perf_counter()
    file_input = read_file("day_7/input.txt")
    parsed_input = parse_input(file_input)
    part1(parsed_input)
    t1 = time.perf_counter()
    print(f"Took {(t1-t0)*1000:.3f} ms")
    part2(parsed_input)
    t2 = time.perf_counter()
    print(f"Took {(t2-t1)*1000:.3f} ms")