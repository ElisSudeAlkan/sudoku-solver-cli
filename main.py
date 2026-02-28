import argparse
from sudoku.io import parse_puzzles
from sudoku.board import Board
from sudoku.validate import is_valid_board
from sudoku.solver import solve_board
from sudoku import metrics

def _print_grid(g):
    for r in range(9):
        print(" ".join(str(x) for x in g[r]))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="puzzles/mixed_formats.txt")
    p.add_argument("--strategy", default="mrv", choices=["naive", "mrv"])
    p.add_argument("--limit", type=int, default=999999)
    p.add_argument("--print-solved", default="true")
    args = p.parse_args()

    boards = parse_puzzles(args.input)[: args.limit]
    solved_count = 0

    for i, b in enumerate(boards):
        orig_line = b.to_line()
        metrics.reset()
        solved = solve_board(b.clone(), strategy=args.strategy)
        snap = metrics.snapshot()

        ok = solved is not None and is_valid_board(solved)
        if ok:
            solved_count += 1

        print("original:", orig_line)
        if ok:
            print("solved:", Board(solved).to_line())
        else:
            print("solved: <none>")

        print("metrics:", snap)

        if args.print_solved.lower() == "true" and ok:
            _print_grid(solved)

    print(f"\nSolved {solved_count}/{len(boards)} puzzles.")

if __name__ == "__main__":
    main()