
from pathlib import Path
from view.pieces.piece_loader import PieceLoader

#עבור כל כלי שומר :סוג, צבע, מצב, ורשימת תמונות
class AnimationLibrary:
    
    """
    Stores all animation frames in memory.

    No disk access during gameplay.
    """
    def __init__(
            self,
            piece_loader: PieceLoader
    ):

        self._piece_loader = piece_loader

        self._animations = {} #תמונות לאנימציות

    def load_animation(
            self,
            kind,
            color,
            state
    ):
        """
        Loads all frames of one animation.
        """

        key = (
            kind,
            color,
            state
        )

        frames_count = self._piece_loader.count_frames(kind, color, state)

        frames = [
            self._piece_loader.load_piece(kind, color, state, i + 1)
            for i in range(frames_count)
        ]

        self._animations[key] = frames



    def get_frame(
            self,
            kind,
            color,
            state,
            frame_index=0
    ):
        """
        Returns a specific frame.
        """


        key = (
            kind,
            color,
            state
        )


        frames = self._animations.get(key)


        if frames is None:
            raise ValueError(
                "Animation was not loaded"
            )


        return frames[
            frame_index % len(frames)
        ]
