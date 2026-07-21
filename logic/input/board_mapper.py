from logic.model.position import Position

CELL_SIZE = 100
#ממיר בין פיקסלים לתאים (עמודה, שורה)
class BoardMapper:
    # מאתחל את הממיר עם גודל הלוח כדי לדעת מתי קואורדינטה מחוץ לגבולות
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols

    # ממיר קואורדינטות פיקסל לתא לוח, מחזיר None אם הקליק מחוץ ללוח
    def pixel_to_cell(self, x: int, y: int)-> Position | None:
        """ממיר קואורדינטות פיקסל לPosition, או None אם מחוץ ללוח."""
        col = x // CELL_SIZE
        row = y // CELL_SIZE
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return Position(row, col)
        return None
