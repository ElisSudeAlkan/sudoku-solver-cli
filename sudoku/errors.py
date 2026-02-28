class SudokuError(Exception):
    pass

class ParseError(SudokuError):
    pass

class InvalidBoardError(SudokuError):
    pass