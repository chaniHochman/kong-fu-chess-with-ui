#ציור הכלים במיקומים הנכונים לפי ה־Snapshot
from UI.graphics.img import Img
import cv2

class PieceRenderer:
    """
    Draws all pieces on the board.
    """
    def __init__(self,
            animation_library,
            piece_animator,
            geometry
            ):

        self._animation_library = animation_library
        self._piece_animator = piece_animator
        self._geometry = geometry


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
        STATE_MAP = {"idle": "idle", "move": "move", "jump": "jump","short_rest":"short_rest","long_rest":"long_rest", "captured": "idle"}

        for piece in snapshot.pieces:


            
            kind=KIND_MAP.get(piece.kind, piece.kind)
            color=COLOR_MAP.get(piece.color, piece.color)
            state=STATE_MAP.get(piece.state, piece.state)
            

            frames_count = self._animation_library.count_frames(
                kind,
                color,
                state
            )
          

              ######
            fps = self._animation_library.get_fps(
                kind,
                color,
                state
            )
            loop = self._animation_library.is_loop(
                kind,
                color,
                state
            )
            ############
            frame_index = self._piece_animator.get_frame_index(
                piece.piece_id,
                frames_count,
                fps,
                loop
            )
            ##############
            sprite = self._animation_library.get_frame(
                kind,
                color,
                state,
                frame_index
                )
            
            position = self._piece_animator.get_position(
                piece.piece_id
                )
            if position is not None:

                x, y = position

            else:

                x = piece.pixel_x
                y = piece.pixel_y

            #שינוי גודל התמונה של הכלי לפי גודל התא
            sprite.img = cv2.resize(
                sprite.img,
                (
                    self._geometry.cell_width,
                    self._geometry.cell_height
                )
            )
        # print(
        #     "piece:",
        #     piece.piece_id,
        #     "position:",
        #     x,
        #     y,
        #     "sprite:",
        #     sprite.width(),
        #     sprite.height(),
        #     "canvas:",
        #     canvas.width(),
        #     canvas.height()
        # )
            sprite.draw_on(
                canvas,
                x,
                y
            )