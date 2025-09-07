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

def DLS(board, depth, limit):
    if is_goal(board):
        return [board]
    if depth == limit:
        return None
    
    for child in generate_children(board):
        path = DLS(child, depth + 1, limit)
        if path:
            return [board] + path
    return None

# Example initial state
initial_state = [[5, 1, 6],
                 [2, 0, 3],
                 [7, 4, 8]]

limit = 20  # depth limit
solution = DLS(initial_state, 0, limit)

if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found within depth limit.")
