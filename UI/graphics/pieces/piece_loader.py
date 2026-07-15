#PieceLoader – טעינת כל הספרייטים לזיכרון.

from pathlib import Path

from view.img import Img
from view.image_utils import ensure_alpha


class PieceLoader:
    """
    Loads chess piece images once and keeps them in memory.
    """


    def __init__(self, assets_root: Path):

        self._assets_root = assets_root

        # כאן נשמור את כל התמונות
        self._images = {}



    def load_piece(
            self,
            kind: str,
            color: str,
            state: str,
            frame: int
    ) -> Img:
        """
        Loads one sprite and returns it.

        If it was already loaded,
        returns the existing object.
        """


        key = (
            kind,
            color,
            state,
            frame
        )


        # כבר קיים בזיכרון
        if key in self._images:
            return self._images[key]



        path = self._build_path(
            kind,
            color,
            state,
            frame
        )


        img = Img()

        img.read(path)

        img.img = ensure_alpha(img.img)#הוספת שקיפות


        self._images[key] = img


        return img



    def _build_path(self,kind,color,state,frame):
        """
        Builds the path to the sprite file.
        """


        folder = (
            kind.upper()
            +
            color.upper()
        )


        return (
            self._assets_root
            /
            folder
            /
            "states"
            /
            state
            /
            "sprites"
            /
            f"{frame}.png"
        )