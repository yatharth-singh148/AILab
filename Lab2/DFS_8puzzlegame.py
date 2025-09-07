from copy import deepcopy

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]   # 0 = blank space

# Moves: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal(board):
    return board == goal_state

def generate_children(board):
    children = []
    x, y = find_blank(board)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = deepcopy(board)
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            children.append(new_board)
    return children

def board_to_tuple(board):
    return tuple(num for row in board for num in row)

def DFS(start):
    stack = [(start, [start])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if is_goal(state):
            return path
        visited.add(board_to_tuple(state))
        for child in generate_children(state):
            if board_to_tuple(child) not in visited:
                stack.append((child, path + [child]))
    return None

# Example initial state
initial_state = [[5, 1, 6],
                 [2, 0, 3],
                 [7, 4, 8]]

solution = DFS(initial_state)

if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
