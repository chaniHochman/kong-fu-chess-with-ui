#ציור הלוח על הקנבס.
# PieceRenderer שואל את PieceAnimator
# איפה הכלי?
#ואז PieceRenderer מצייר אותו.

from view.img import Img

from view.protocols import Renderer
#בעתיד ניתן להוסיף ציורים על הלוח.

class BoardRenderer(Renderer):
    """
    Responsible for drawing the board.

    The board image itself is provided by BoardLoader.
    """


    def __init__(self, board_loader):

        self._board_loader = board_loader



    def render(self, canvas: Img, snapshot) -> None:
        """
        Draws the board background.
        """

        board = self._board_loader.get_image()

        board.draw_on(
            canvas,
            0,
            0
        )