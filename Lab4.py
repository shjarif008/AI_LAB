import heapq

# Goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            curr_row, curr_col = divmod(i, 3)
            goal_row, goal_col = divmod(state[i] - 1, 3)
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# Generate neighbors
def get_neighbors(state):
    neighbors = []
    blank_pos = state.index(0)
    row, col = divmod(blank_pos, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row <= 2 and 0 <= new_col <= 2:
            new_blank = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_pos], new_state[new_blank] = \
                new_state[new_blank], new_state[blank_pos]
            neighbors.append(tuple(new_state))

    return neighbors

# A* Search
def a_star_search(start_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, [start_state]))

    visited = set()

    while pq:
        f, g, current_state, path = heapq.heappop(pq)

        if current_state == goal_state:
            return path

        if current_state in visited:
            continue

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# Print state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# MAIN EXECUTION
initial_state = (8, 2, 3, 4, 0, 5, 6, 1, 7)

print("Initial State:")
print_state(initial_state)

solution_path = a_star_search(initial_state)

if solution_path:
    print("Solution found! Path length:", len(solution_path) - 1)
    print("Path to goal:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        print_state(state)
else:
    print("No solution found.")
