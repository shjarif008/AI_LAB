import heapq

# Goal state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Function of Manhattan Distance
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0: 
            curr_row, curr_col = divmod(i, 3) 
            tile = state[i] 
            goal_row, goal_col = divmod(tile - 1, 3)
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

# Function to get neighbors of a state
def get_neighbors(state):
    neighbors = []
    blank_pos = state.index(0)
    row, col = divmod(blank_pos, 3)
    
    # Possible moves-up down left right
    directions = [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]
    
    for dr, dc, _ in directions:
        new_row, new_col = row + dr, col + dc
        if 0<=new_row<=2 and 0<=new_col<=2:
            new_blank_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_pos], new_state[new_blank_pos] = new_state[new_blank_pos], new_state[blank_pos]
            neighbors.append(tuple(new_state))
    
    return neighbors

# Best-First Search
def best_first_search(start_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start_state), start_state, [start_state]))
    
    # Visited set to avoid revisiting states
    visited = set()
    visited.add(start_state)
    
    while pq:
        _, current_state, path = heapq.heappop(pq)
        
        if current_state == goal_state:
            return path 
        
        # Generate neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                heapq.heappush(pq, (manhattan_distance(neighbor), neighbor, new_path))
    
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
    
solution_path = best_first_search(initial_state)
    
if solution_path:
    print("Solution found! Path length:", len(solution_path) - 1)
    print("Path to goal:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        print_state(state)   
else:
    print("No solution found.")
