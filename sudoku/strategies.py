from sudoku.candidates import all_candidates

def pick_next_cell(board, strategy):
    # strategy is a string: "naive" or "mrv"
    if strategy == "naive":
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return None

    if strategy == "mrv":
        cand = all_candidates(board)
        if not cand:
            return None
        items = list(cand.items())
        items.sort(key=lambda kv: len(kv[1]))
        return items[0][0]

    # fallback to naive
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None