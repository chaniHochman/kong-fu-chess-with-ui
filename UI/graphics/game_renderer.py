from __future__ import annotations
from pathlib import Path
from img import Img
from model.position import Position

#מחזיר את התמונה של הלוח עם הכלים במקומם בהתאם למצב הנוכחי של הלוח

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
BOARD_IMAGE = ASSETS_DIR / "board.png"
PIECES_DIR = ASSETS_DIR / "pieces1"
PIECE_KINDS = {
    "pawn": "P",
    "rook": "R",
    "knight": "N",
    "bishop": "B",
    "queen": "Q",
    "king": "K",
}
DEFAULT_STATE = "idle"


# מחזיר את התיקייה של סוג הכלי בהתאם לצבעו ולסוגו
def _piece_type_folder(piece) -> Path:
    kind_code = PIECE_KINDS.get(piece.kind)
    if kind_code is None:
        raise ValueError(f"unsupported piece kind: {piece.kind}")
    color_code = piece.color[0].upper()
    return PIECES_DIR / f"{kind_code}{color_code}"


# מחזיר את התיקייה המתאימה למצב הנוכחי של הכלי (idle, jump וכדומה)
def _piece_state_folder(piece) -> Path:
    state_name = getattr(piece, "state", DEFAULT_STATE) or DEFAULT_STATE
    state_folder = _piece_type_folder(piece) / "states" / state_name
    if not state_folder.exists():
        state_folder = _piece_type_folder(piece) / "states" / DEFAULT_STATE
    return state_folder


# מחזיר את הנתיב לקובץ הספרייט של הכלי בתוך תיקיית המצב שלו
def _piece_sprite_path(piece) -> Path:
    state_folder = _piece_state_folder(piece) / "sprites"
    candidates = sorted(state_folder.glob("*.png"))
    if not candidates:
        raise FileNotFoundError(f"No sprite found for piece in {state_folder}")
    first_choice = state_folder / "1.png"
    return first_choice if first_choice.exists() else candidates[0]


# טוען את ספרייט הכלי ומתאים אותו לגודל משבצת הלוח
def _load_piece_sprite(piece, tile_size: int) -> Img:
    sprite_path = _piece_sprite_path(piece)
    return Img().read(sprite_path, size=(tile_size, tile_size), keep_aspect=True)


# מצייר את לוח המשחק על התמונה של board.png ומניח את הספרייטים של הכלים במקומם
def draw_board(board, board_path: str | Path | None = None, size: tuple[int, int] | None = None) -> Img:
    """Render the current board using the assets board image and piece sprites."""
    board_path = Path(board_path) if board_path is not None else BOARD_IMAGE
    canvas = Img().read(board_path, size=size)

    if board.cols == 0 or board.rows == 0:
        raise ValueError("Board must have positive rows and cols")

    tile = min(canvas.width(), canvas.height()) // board.cols
    x_offset = (canvas.width() - tile * board.cols) // 2
    y_offset = (canvas.height() - tile * board.rows) // 2

    for row in range(board.rows):
        for col in range(board.cols):
            piece = board.get_piece(Position(row, col))
            if piece is None:
                continue

            sprite = _load_piece_sprite(piece, tile)
            x = x_offset + col * tile
            y = y_offset + row * tile
            sprite.draw_on(canvas, x, y)
            #canvas.put_text(name,score)
            canvas.show()
    return canvas
