#טעינת board.png פעם אחת.
from pathlib import Path

from view.img import Img
from view.geometry import BoardGeometry
from view.image_utils import ensure_alpha


class BoardLoader:
    """
    Responsible only for loading the board image.

    It loads once and provides clean copies
    for every frame.
    """

    def __init__(self, image_path: Path, geometry: BoardGeometry):

        self._image_path = image_path
        self._geometry = geometry
        self._board_image = None

    def load(self) -> None:
        """
        Loads the board image from disk.
        """
        if self._board_image is None:

            self._board_image = Img()

            self._board_image.read(
                self._image_path,
                size=(
                    self._geometry.window_width,
                    self._geometry.window_height
                )
            )
            return self._board_image
        # img.img = ensure_alpha(img.img)#תמונה עם שקיפות

        # self._board_image = img



    
    def get_image(self):

        return self.board_image



    # def reload(self) -> None:
    #     """
    #     Reloads the board after window resize.
    #     """

    #     self.load()