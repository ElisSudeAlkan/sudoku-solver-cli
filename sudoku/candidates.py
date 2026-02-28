def can_place(board, row, col, num):
    # duplicates validate logic
    for c in range(9):
        if board[row][c] == num:
            return False
    for r in range(9):
        if board[r][col] == num:
            return False
    sr = row - row % 3
    sc = col - col % 3
    for r in range(sr, sr+3):
        for c in range(sc, sc+3):
            if board[r][c] == num:
                return False
    return True

def get_candidates(board, row, col):
    if board[row][col] != 0:
        return []
    out = []
    for n in range(1, 10):
        if can_place(board, row, col, n):
            out.append(n)
    return out

def all_candidates(board):
    # recompute everything every time (slow)
    m = {}
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                m[(r,c)] = get_candidates(board, r, c)
    return m