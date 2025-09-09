def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        new_state = [row[:] for row in state]
                        new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                        neighbors.append(new_state)
                break
    return neighbors

def hill_climbing(initial, goal):
    current = initial
    path = [current]
    while current != goal:
        neighbors = get_neighbors(current)
        if not neighbors:
            return None, path
        best_neighbor = min(neighbors, key=lambda x: misplaced_tiles(x, goal))
        if misplaced_tiles(best_neighbor, goal) >= misplaced_tiles(current, goal):
            return None, path
        current = best_neighbor
        path.append(current)
    return current, path

def print_state(state):
    for row in state:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

initial_state = [
    [1, 2, 3],
    [8, 6, 0],
    [7, 5, 4]
]
goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution, path = hill_climbing(initial_state, goal_state)
if solution:
    print("Solution found:")
    for state in path:
        print_state(state)
else:
    print("No solution found.")
