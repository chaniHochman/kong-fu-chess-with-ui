class PieceSnapshot:#מצב המשחק
    # תמונת מצב של כלי בודד לקריאה בלבד
    def __init__(self, piece_id,kind, color, pixel_x, pixel_y, state,image):
        self.kind = kind
        self.color = color
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.state = state
        self.image=image
        self.piece_id=piece_id

class GameSnapshot:
    # תמונת מצב של המשחק כולו, מועברת ל-Renderer בלבד
    def __init__(self, board_width, board_height, pieces, selected_cell, game_over):
        self.board_width = board_width
        self.board_height = board_height
        self.pieces = pieces          # רשימת PieceSnapshot
        self.selected_cell = selected_cell  # Position או None
        self.game_over = game_over
