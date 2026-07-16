#ציור הכלים במיקומים הנכונים לפי ה־Snapshot
from view.img import Img


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


        for piece in snapshot.pieces:


            sprite = self._animation_library.get_frame(
                piece.kind,
                piece.color,
                piece.state
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