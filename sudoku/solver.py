from sudoku.candidates import get_candidates
from sudoku.strategies import pick_next_cell
from sudoku.validate import is_valid_board
from sudoku import metrics

def solve_board(board_obj, strategy="naive"):
    metrics.start()
    grid = board_obj.as_grid()

    if not is_valid_board(grid):
        return None

    result = _solve(grid, strategy)

    return result

def _solve(board, strategy):
    metrics.inc_nodes()

    nxt = pick_next_cell(board, strategy)
    if nxt is None:
        # solved
        return board

    r, c = nxt

    cand = get_candidates(board, r, c)
    if len(cand) == 0:
        metrics.inc_backtrack()
        return None

    # try numbers
    for n in cand:
        board[r][c] = n

        # extra validation check (wasteful but works)
        if is_valid_board(board):
            out = _solve(board, strategy)
            if out is not None:
                return out

        board[r][c] = 0

    metrics.inc_backtrack()
    return None