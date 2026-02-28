from sudoku.errors import ParseError
from sudoku.board import Board

def _digits_only(s):
    return "".join(ch for ch in s if ch.isdigit())

def parse_puzzles(path):
    """
    Supports:
    - 9 lines of 9 digits
    - single line of 81 digits
    - blank lines and comments starting with '#'
    Returns list[Board]
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]

    cleaned = []
    for ln in lines:
        if not ln.strip():
            cleaned.append("")  # keep separators
            continue
        if ln.strip().startswith("#"):
            continue
        cleaned.append(ln)

    boards = []
    buf = []
    for ln in cleaned:
        if ln == "":
            if buf:
                boards.append(_parse_buf(buf))
                buf = []
            continue
        buf.append(ln)

    if buf:
        boards.append(_parse_buf(buf))

    return boards

def _parse_buf(buf):
    if len(buf) == 1:
        s = _digits_only(buf[0])
        if len(s) != 81:
            raise ParseError(f"Expected 81 digits, got {len(s)}")
        return Board(s)
    if len(buf) == 9:
        grid = []
        for ln in buf:
            s = _digits_only(ln)
            if len(s) != 9:
                raise ParseError("Each row must have 9 digits")
            grid.append([int(ch) for ch in s])
        return Board(grid)
    raise ParseError(f"Unrecognized puzzle format with {len(buf)} lines")