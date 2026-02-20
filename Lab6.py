# Goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance heuristic
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

# Hill Climbing Search
def hill_climbing(start_state):
    current = start_state
    current_h = manhattan_distance(current)
    path = [current]

    while True:
        neighbors = get_neighbors(current)
        next_state = current
        next_h = current_h

        for neighbor in neighbors:
            h = manhattan_distance(neighbor)
            if h < next_h:
                next_state = neighbor
                next_h = h

        if next_h >= current_h:
            break

        current = next_state
        current_h = next_h
        path.append(current)

        if current == goal_state:
            break

    return path

# Print puzzle
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# MAIN
initial_state = (8, 2, 3, 4, 0, 5, 6, 1, 7)

print("Initial State:")
print_state(initial_state)

solution = hill_climbing(initial_state)

print("Hill Climbing Result:")
for step, state in enumerate(solution):
    print(f"Step {step}:")
    print_state(state)

if solution[-1] == goal_state:
    print("Goal state reached!")
else:
    print("Stopped at a local minimum.")
