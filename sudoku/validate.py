def row_ok(board, r):
    seen = set()
    for c in range(9):
        v = board[r][c]
        if v == 0:
            continue
        if v in seen:
            return False
        seen.add(v)
    return True

def col_ok(board, c):
    seen = set()
    for r in range(9):
        v = board[r][c]
        if v == 0:
            continue
        if v in seen:
            return False
        seen.add(v)
    return True

def box_ok(board, br, bc):
    seen = set()
    for r in range(br, br+3):
        for c in range(bc, bc+3):
            v = board[r][c]
            if v == 0:
                continue
            if v in seen:
                return False
            seen.add(v)
    return True

def is_valid_board(board):
    for r in range(9):
        if not row_ok(board, r):
            return False
    for c in range(9):
        if not col_ok(board, c):
            return False
    for br in (0,3,6):
        for bc in (0,3,6):
            if not box_ok(board, br, bc):
                return False
    return True