import time

INPUT = "input"

with open(f"day_6/{INPUT}.txt", "r") as f:
    data = [[char for char in line] for line in f.read().splitlines()]

# 0 = up, 1 = right, 2 = down, 3 = left

class Guard():
    def __init__(self, route_map):
        self.route_map: list[list[int]] = route_map
        self.directions_map = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        self.direction: int = 0
        self.position: list[int] = self.find_starting_position()
        self.visited: dict = {tuple(self.position): {self.direction}}
        self.inf_loop = False

    def start_patrol(self):
        while self.inf_loop == False:
            try:
                self.step()
                if tuple(self.position) not in self.visited:
                    self.visited[tuple(self.position)] = {self.direction}
                else:
                    if self.direction not in self.visited[tuple(self.position)]:
                        self.visited[tuple(self.position)].add(self.direction)
                    else:
                        self.inf_loop = True
            except IndexError:
                break
            

    def find_starting_position(self):
        for y, row in enumerate(self.route_map):
            for x, cell in enumerate(row):
                if cell == "^":
                    return (y, x)
                
    def step(self):
        next_tile_location = [
            self.position[0] + self.directions_map[self.direction][0],
            self.position[1] + self.directions_map[self.direction][1],
        ]

        if not (0 <= next_tile_location[0] < len(self.route_map) and
                0 <= next_tile_location[1] < len(self.route_map[0])):
            raise IndexError
      
        next_tile = self.route_map[next_tile_location[0]][next_tile_location[1]]
        if next_tile == "#":
            self.turn_right()
        else:
            self.position = next_tile_location
        
    def turn_right(self):
        self.direction = (self.direction + 1) % 4

def create_run_guard(data):               
    guard = Guard(data)
    guard.start_patrol()
    return guard

t0 = time.perf_counter()

guard = create_run_guard(data)
all_tiles_visited = set(guard.visited.keys())

t1 = time.perf_counter()
print(f"Part One: {len(all_tiles_visited)}, took {(t1-t0)*1000:,.3f} ms")

loop_options = 0

for y, x in all_tiles_visited:
    if data[y][x] == ".":
        data[y][x] = "#"
        guard = create_run_guard(data)
        if guard.inf_loop:
            loop_options += 1
        data[y][x] = "."
t2 = time.perf_counter()

print(f"Part Two: {loop_options}, took {(t2-t1):.3f} s")
