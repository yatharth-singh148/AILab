from copy import deepcopy

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

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

def DLS(board, depth, limit, visited):
    if is_goal(board):
        return [board]
    if depth == limit:
        return None

    visited.add(board_to_tuple(board))

    for child in generate_children(board):
        t = board_to_tuple(child)
        if t not in visited:
            result = DLS(child, depth + 1, limit, visited)
            if result:
                return [board] + result

    visited.remove(board_to_tuple(board))
    return None

# Example initial state
initial_state = [[5, 1, 6],
                 [2, 0, 3],
                 [7, 4, 8]]

limit = 20
solution = DLS(initial_state, 0, limit, set())

if solution:
    print("Solution found!")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found within depth limit.")
