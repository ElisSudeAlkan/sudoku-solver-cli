from dataclasses import dataclass

@dataclass
class Board:
    raw: object  # sometimes str, sometimes list[list[int]]

    def as_grid(self):
        if isinstance(self.raw, list):
            return self.raw
        # raw is a string of digits length 81
        s = str(self.raw).strip()
        g = []
        for r in range(9):
            row = []
            for c in range(9):
                row.append(int(s[r*9 + c]))
            g.append(row)
        self.raw = g
        return g

    def clone(self):
        g = self.as_grid()
        return Board([row[:] for row in g])

    def to_line(self):
        g = self.as_grid()
        out = []
        for r in range(9):
            for c in range(9):
                out.append(str(g[r][c]))
        return "".join(out)