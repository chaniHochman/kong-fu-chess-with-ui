"""
מחלקה האחראית על טעינת כל קבצי הגרפיקה.

המחלקה קוראת פעם אחת בלבד:

• כל התמונות
• כל קבצי ה-JSON

ויוצרת עבור כל מצב Animation מוכן לשימוש.
"""

import json
from pathlib import Path

from graphics.img import Img
from graphics.animation import Animation

class AssetLoader:

    """
    רשימת המצבים האפשריים של כל כלי.
    """

    STATES = [
        "idle",
        "move",
        "jump",
        "short_rest",
        "long_rest"
    ]

    # ----------------------------------------------------------

    """
    יוצר טוען Assets חדש.

    Parameters
    ----------
    assets_folder : str
        הנתיב לתיקיית pieces1.

    square_size : int
        גודל המשבצת בלוח.
        כל התמונות ישונו לגודל זה.
    """

    def __init__(self,
                 assets_folder="assets/pieces1",
                 square_size=90):

        self.assets_folder = Path(assets_folder)

        self.square_size = square_size

        # token -> state -> Animation
        self.animations = {}

    # ----------------------------------------------------------

    """
    טוען את כל הכלים וכל המצבים שלהם לזיכרון.

    הפונקציה עוברת על כל התיקיות:

    KW
    KB
    QW
    QB
    ...

    ובכל אחת מהן טוענת את כל המצבים.
    """

    def load_assets(self):

        for piece_folder in self.assets_folder.iterdir():

            if not piece_folder.is_dir():
                continue

            piece_token = piece_folder.name

            self.animations[piece_token] = {}

            for state in self.STATES:

                state_folder = (
                        piece_folder /
                        "states" /
                        state
                )

                if not state_folder.exists():
                    continue

                animation = self._load_state(state_folder)

                self.animations[piece_token][state] = animation

    # ----------------------------------------------------------

    """
    טוען מצב אחד של כלי.

    לדוגמה:

    idle

    או

    move

    הפונקציה קוראת:

    • config.json
    • כל קבצי ה-PNG

    ומחזירה Animation מוכן.
    """

    def _load_state(self, state_folder):

        config_file = state_folder / "config.json"

        with open(config_file,
                  encoding="utf8") as file:

            config = json.load(file)

        fps = config["graphics"]["frames_per_sec"]

        is_loop = config["graphics"]["is_loop"]

        sprite_folder = state_folder / "sprites"

        frames = []

        png_files = sorted(
            sprite_folder.glob("*.png"),
            key=lambda file: int(file.stem)
        )

        for image_path in png_files:

            frame = Img().read(
                image_path,
                size=(
                    self.square_size,
                    self.square_size
                ),
                keep_aspect=True
            )

            frames.append(frame)

        return Animation(
            frames,
            fps,
            is_loop
        )

    # ----------------------------------------------------------

    """
    מחזיר את האנימציה המתאימה לכלי ולמצב המבוקש.

    Parameters
    ----------
    piece_token : str
        לדוגמה:
        KW
        QB
        PB

    state : str
        לדוגמה:
        idle
        move
        jump

    Returns
    -------
    Animation
    """

    def get_animation(self,
                      piece_token,
                      state):

        return self.animations[piece_token][state]

