import heapq

goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def heuristic(state):
    return sum(abs((val % 3) - (i % 3)) + abs((val // 3) - (i // 3)) for i, row in enumerate(state) for j, val in enumerate(row) if val != 0)

def valid_moves(pos):
    row, col = pos
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return [(row + dr, col + dc) for dr, dc in moves if 0 <= row + dr < 3 and 0 <= col + dc < 3]

def swap(state, pos1, pos2):
    state = [list(row) for row in state]
    state[pos1[0]][pos1[1]], state[pos2[0]][pos2[1]] = state[pos2[0]][pos2[1]], state[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in state)

def astar(start):
    open_list = []
    closed_set = set()
    start_pos = next((r, c) for r, row in enumerate(start) for c, val in enumerate(row) if val == 0)
    heapq.heappush(open_list, (heuristic(start), 0, start, start_pos, []))
    
    while open_list:
        _, g, current, zero_pos, path = heapq.heappop(open_list)
        
        if current == goal:
            return path
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        for move in valid_moves(zero_pos):
            new_state = swap(current, zero_pos, move)
            if new_state not in closed_set:
                heapq.heappush(open_list, (g + 1 + heuristic(new_state), g + 1, new_state, move, path + [new_state]))
    return []

start = ((5, 4, 0), (6, 1, 8), (7, 3, 2))
solution = astar(start)
solution
