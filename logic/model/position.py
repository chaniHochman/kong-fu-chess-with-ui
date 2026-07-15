class Position:#תא לוח
    def __init__(self, row: int, col: int):
        """ייצר מיקום חדש בשורה ובעמודה נתונים."""
        if not isinstance(row, int):
            raise TypeError("row must be an int")
        if not isinstance(col, int):
            raise TypeError("col must be an int")

        self.row = row
        self.col = col

    def __eq__(self, other):
        """בודק אם שני מיקומים זהים על סמך שורה ועמודה."""
        if not isinstance(other, Position):
            return NotImplemented
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        """מחזיר ייצוג קריא של המיקום לצורך הדפסה וניתוח."""
        return f"Position(row={self.row}, col={self.col})"
