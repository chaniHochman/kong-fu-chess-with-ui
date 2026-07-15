#יצירת לוח מטקסט
from model.board import Board
from model.position import Position
from model.piece import Piece


# קורא טקסט לוח ומחזיר מטריצה של תאים (כפי שמצופה במבחנים הישנים)
class BoardParser:
    # מחזיר רשימת שורות של טוקנים (לדוגמה [['wR', '.'], ['.', 'bP']])
    def parse_board(self, text: str):
        lines = text.strip().splitlines()
        if not lines:
            raise ValueError("ERROR EMPTY_BOARD")
        rows_data = []
        # המרת שורות למערכים של תאים
        for line in lines:
            row = line.strip().split()
            rows_data.append(row)

        # בדיקה שכל השורות באותו אורך
        cols = len(rows_data[0])
        for row in rows_data:
            if len(row) != cols:
                raise ValueError("ERROR ROW_WIDTH_MISMATCH")

        # רשימת סמלים תקינים
        valid = {"."}
        for color in ("w", "b"):
            for piece in ("K", "Q", "R", "B", "N", "P"):
                valid.add(color + piece)

        for r, row in enumerate(rows_data):
            for c, cell in enumerate(row):
                if cell not in valid:
                    raise ValueError("ERROR UNKNOWN_TOKEN")

        return rows_data

    # המרה ל־Board עם אובייקטי Piece (שימוש ליישום, לא למבחנים הוותיקים)
    def parse_to_board(self, text: str) -> Board:
        rows = self.parse_board(text)
        rows_count = len(rows)
        cols = len(rows[0])
        board = Board(rows_count, cols)

        # בחר מזהה ייחודי שאינו בשימוש
        next_id = 1
        if Piece._used_ids:
            next_id = max(Piece._used_ids) + 1

        # מיפוי מסמך קצר לייצוג פנימי
        kind_map = {
            "K": "king",
            "Q": "queen",
            "R": "rook",
            "B": "bishop",
            "N": "knight",
            "P": "pawn",
        }
        color_map = {"w": "white", "b": "black"}
        #יצירת לוח עם אובייקטי Piece
        for r, row in enumerate(rows):
            for c, cell in enumerate(row):
                if cell == ".":
                    continue
                color = color_map[cell[0]]
                kind = kind_map[cell[1]]
                pos = Position(r, c)
                piece = Piece(id=next_id, color=color, kind=kind, cell=pos)
                next_id += 1
                board.add_piece(piece, pos)

        return board