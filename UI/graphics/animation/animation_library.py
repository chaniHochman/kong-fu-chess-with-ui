
from pathlib import Path
from UI.graphics.pieces.piece_loader import PieceLoader
import json
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

        #self._animations[key] = frames
############################
    # טעינת config של המצב
        config = self._piece_loader.load_config(
            kind,
            color,
            state
        )

###################################33
    # שמירת הכל בזיכרון
        self._animations[key] = {
            "frames": frames,
            "fps": config["graphics"]["frames_per_sec"],
            "loop": config["graphics"]["is_loop"],
            "next_state": config["physics"]["next_state_when_finished"]
        }

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


        animation  = self._animations.get(key)


        if animation  is None:
            raise ValueError(
                "Animation was not loaded"
            )
        frames = animation["frames"]

        return frames[
            frame_index % len(frames)
        ]
    ###########
    def count_frames(
            self,
            kind,
            color,
            state
        ):

        key = (
            kind,
            color,
            state
        )

        animation = self._animations.get(key)

        if animation is None:
            return 1

        frames = animation["frames"]

        return len(frames)
    






###########################

    def get_fps(
        self,
        kind,
        color,
        state
    ):
        key = (kind, color, state)

        return self._animations[key]["fps"]



    def is_loop(
            self,
            kind,
            color,
            state
    ):
        key = (kind, color, state)

        return self._animations[key]["loop"]



    def get_next_state(
            self,
            kind,
            color,
            state
    ):
        key = (kind, color, state)

        return self._animations[key]["next_state"]