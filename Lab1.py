# Goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# Function to get neighbors of a state
def get_neighbors(state):
    neighbors = []
    blank_pos = state.index(0)
    row, col = divmod(blank_pos, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row <= 2 and 0 <= new_col <= 2:
            new_blank_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_pos], new_state[new_blank_pos] = (
                new_state[new_blank_pos],
                new_state[blank_pos],
            )
            neighbors.append(tuple(new_state))
    return neighbors

# Breadth-First Search
def bfs(start_state):
    queue = deque()
    queue.append((start_state, [start_state]))

    visited = set()
    visited.add(start_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Function to print the 3x3 state
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# MAIN EXECUTION
initial_state = (8, 2, 3, 4, 0, 5, 6, 1, 7)
print("Initial State:")
print_state(initial_state)
solution_path = bfs(initial_state)

if solution_path:
    print("Solution found! Path length:", len(solution_path) - 1)
    print("Path to goal:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        print_state(state)
else:
    print("No solution found.") 
