#ציור הכלים במיקומים הנכונים לפי ה־Snapshot
from view.img import Img


class PieceRenderer:
    """
    Draws all pieces on the board.
    """
    def __init__(
            self,
            animation_library
    ):

        self._animation_library = animation_library



    def render(
            self,
            canvas: Img,
            snapshot
    ) -> None:
        """
        Draws every piece from the snapshot.
        """


        for piece in snapshot.pieces:


            sprite = self._animation_library.get_frame(
                piece.kind,
                piece.color,
                piece.state
            )


            sprite.draw_on(
                canvas,
                piece.pixel_x,
                piece.pixel_y
            )