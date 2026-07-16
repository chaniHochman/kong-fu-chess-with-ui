from logic.model.board import Board
from logic.model.position import Position


# מדפיס אובייקט `Board` חזרה לפורמט טקסט
class BoardPrinter:
    # בונה מדפיס שמקבל אובייקט Board
    def __init__(self, board: Board):
        self.board = board

    # מחזיר מחרוזת טקסט המייצגת את הלוח
    def render(self) -> str:
        rows = []
        for r in range(self.board.rows):
            display = []
            for c in range(self.board.cols):
                piece = self.board.get_piece(Position(r, c))
                if piece is None:
                    display.append(".")
                else:
                    # המחזיר תוי קצר כמו 'wR' או 'bP'
                    short = ("w" if piece.color == "white" else "b")
                    kind_map = {
                        "king": "K",
                        "queen": "Q",
                        "rook": "R",
                        "bishop": "B",
                        "knight": "N",
                        "pawn": "P",
                    }
                    short += kind_map.get(piece.kind, "?")
                    display.append(short)
            rows.append(" ".join(display))
        return "\n".join(rows)

    # הדפסה ישירה ל־stdout
    def print_board(self):
        print(self.render())