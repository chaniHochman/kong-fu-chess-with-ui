from model.piece import Piece
from model.position import Position


class Board:
    """אחראי על האחסון הלוגי של הכלים על הלוח ובדיקת גבולות התאים."""

    def __init__(self, rows: int, cols: int):
        """יוצר לוח עם גודל שורות ועמודות נתון."""
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise TypeError("rows and cols must be ints")
        if rows <= 0 or cols <= 0:
            raise ValueError("rows and cols must be positive")

        self.rows = rows
        self.cols = cols
        self._grid = [[None for _ in range(cols)] for _ in range(rows)]#יצירת מטריצה דו-ממדית של None כדי לייצג תאים ריקים על הלוח

    def add_piece(self, piece: Piece, position: Position):
        """מוסיף כלי לתא מסוים אם התא פנוי."""
        # self._validate_piece(piece)
        self._validate_position(position)
        #אם התא כבר תפוס, זרוק חריגה        
        if self.get_piece(position) is not None:
            raise ValueError("cell is already occupied")
        #הוספת הכלי לתא והגדרת המיקום שלו
        self._grid[position.row][position.col] = piece
        piece.cell = position

    def remove_piece(self, position: Position):
        """מסיר כלי מהתא הנתון אם קיים."""
        self._validate_position(position)
        self._grid[position.row][position.col] = None

    def get_piece(self, position: Position):
        """מחזיר את הכלי שבתא הנתון, או None אם התא ריק."""
        self._validate_position(position)
        return self._grid[position.row][position.col]

    def is_within_bounds(self, position: Position):
        """בודק האם התא נמצא בתוך גבולות הלוח."""
        if not isinstance(position, Position):
            raise TypeError("position must be a Position")
        return 0 <= position.row < self.rows and 0 <= position.col < self.cols

    def move_piece(self, source: Position, destination: Position):
        """מזיז כלי ממקור ליעד לאחר שאימות המהלך כבר בוצע."""
        self._validate_position(source)
        self._validate_position(destination)

        piece = self.get_piece(source)
        if piece is None:
            raise ValueError("source cell is empty")

        self._grid[source.row][source.col] = None
        self._grid[destination.row][destination.col] = piece
        piece.cell = destination

    def _validate_position(self, position: Position):
        """מאמת שPosition תקין ושאינו מחוץ לגבולות הלוח."""
        if not isinstance(position, Position):
            raise TypeError("position must be a Position")
        if not self.is_within_bounds(position):
            raise ValueError("position is out of bounds")

    # def _validate_piece(self, piece: Piece):
    #     """מאמת שהכלי הוא אובייקט Piece."""
    #     if not isinstance(piece, Piece):
    #         raise TypeError("piece must be a Piece")
