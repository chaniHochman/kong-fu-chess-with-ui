# הוא לא מצייר בעצמו.

# הוא רק אומר לכל אחד מתי לעבוד.isplayManager – חיבור הכול: לולאת המשחק, עדכון (update), ציור (render), קליטת עכבר והצגת המסך.
import cv2
from UI.graphics.img import Img
from UI.graphics.config import FRAME_DELAY_MS
class DisplayManager:

    def __init__(
        self,
        game_engine,
        board_loader,
        board_renderer,
        piece_renderer,
        piece_animator,
        score_renderer,
        moves_renderer,
        mouse_extractor,
        command_sender
    ):

        self._game_engine = game_engine

        self._board_loader = board_loader

        self._piece_animator = piece_animator

        self._mouse_extractor = mouse_extractor

        self._command_sender = command_sender
        
        self._window_name = "KungFu Chess"
        
        self._renderers = [
            board_renderer,
            piece_renderer,
            score_renderer,
            moves_renderer
            ]

    #update the game
    def update(self):

        self._game_engine.wait(FRAME_DELAY_MS)

        self._piece_animator.update(FRAME_DELAY_MS)

    #build one frame
    def render(self):

        canvas = self._board_loader.get_image().copy()

        snapshot = self._game_engine.create_snapshot()
   
        for renderer in self._renderers:
            if renderer is not None:
                renderer.render(canvas, snapshot)
        
        return canvas
  
    
    def _mouse_callback(
        self,
        event,
        x,
        y,
        flags,
        param
        ):
        command=None
        if event == cv2.EVENT_LBUTTONDOWN:

            command = self._mouse_extractor.extract_left_click(
                x,
                y
            )


        elif event == cv2.EVENT_RBUTTONDOWN:

            command = self._mouse_extractor.extract_right_click(
                x,
                y
            )

        if command is not None:

            self._command_sender.send(command)
    
    def show_frame(self,canvas):
        cv2.imshow("KungFu Chess", canvas.img)
    
    def run(self):
        cv2.namedWindow(self._window_name)
        cv2.setMouseCallback(self._window_name, self._mouse_callback)
        while not self._game_engine.is_game_over():
            self.update()
            canvas = self.render()
            self.show_frame(canvas)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cv2.destroyAllWindows()