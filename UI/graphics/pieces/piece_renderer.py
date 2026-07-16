#ציור הכלים במיקומים הנכונים לפי ה־Snapshot
from UI.graphics.img import Img


class PieceRenderer:
    """
    Draws all pieces on the board.
    """
    def __init__(self,
            animation_library,
            piece_animator
            ):

        self._animation_library = animation_library
        self._piece_animator = piece_animator


    def render(
            self,
            canvas: Img,
            snapshot
            ) -> None:
        """
        Draws every piece from the snapshot.
        """


        KIND_MAP = {"king": "K", "queen": "Q", "rook": "R", "bishop": "B", "knight": "N", "pawn": "P"}
        COLOR_MAP = {"white": "W", "black": "B"}
        STATE_MAP = {"idle": "idle", "moving": "move", "jumping": "jump", "captured": "idle"}

        for piece in snapshot.pieces:


            sprite = self._animation_library.get_frame(
                KIND_MAP.get(piece.kind, piece.kind),
                COLOR_MAP.get(piece.color, piece.color),
                STATE_MAP.get(piece.state, piece.state)
                )


            position = self._piece_animator.get_position(
                piece.piece_id
                )


            if position is not None:

                x, y = position

            else:

                x = piece.pixel_x
                y = piece.pixel_y


            sprite.draw_on(
                canvas,
                x,
                y
            )