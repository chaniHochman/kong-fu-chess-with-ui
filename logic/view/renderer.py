from logic.input.board_mapper import CELL_SIZE

class Renderer:
    # מקבל ממשק ציור עטוף ומצייר את המשחק לפי GameSnapshot
    def __init__(self, image_view):
        self._view = image_view

    # נקודת כניסה ראשית — מצייר רשת, כלים והודעת סיום לפי הסדר
    def render(self, snapshot):
        self._draw_grid(snapshot.board_width, snapshot.board_height)
        self._draw_pieces(snapshot.pieces, snapshot.selected_cell)
        if snapshot.game_over:  #אם המשחק נגמר
            self._draw_game_over()

    # מצייר את רשת הלוח לפי מספר השורות והעמודות
    def _draw_grid(self, width, height):
        for row in range(height):
            for col in range(width):
                self._view.draw_cell(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE)

    # מצייר כל כלי במיקום הפיקסל שלו, מדגיש את הנבחר, מדלג על שבויים
    def _draw_pieces(self, pieces, selected_cell):
        for p in pieces:
            if p.state == "captured":#אם הוא נתפס
                continue
            highlight = (
                selected_cell is not None and
                p.pixel_x == selected_cell.col * CELL_SIZE and
                p.pixel_y == selected_cell.row * CELL_SIZE and
                p.state == "idle"
            )
            self._view.draw_piece(p.image, p.pixel_x, p.pixel_y, highlight)

    # מציג הודעת סיום משחק מעל הלוח
    def _draw_game_over(self):
        self._view.draw_message("Game Over")
