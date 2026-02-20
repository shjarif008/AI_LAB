import heapq

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(state[i] - 1, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

# Get neighboring states
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    r, c = divmod(blank, 3)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]
            neighbors.append(tuple(new_state))
    return neighbors

# AO* Search (adapted for 8-puzzle)
def ao_star(start_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, [start_state]))
    closed = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal_state:
            return path

        closed.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in closed:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# Print puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# MAIN
initial_state = (8, 2, 3, 4, 0, 5, 6, 1, 7)

print("Initial State:")
print_state(initial_state)

solution = ao_star(initial_state)

if solution:
    print("Solution found! Steps:", len(solution) - 1)
    for i, s in enumerate(solution):
        print(f"Step {i}:")
        print_state(s)
else:
    print("No solution found.")
