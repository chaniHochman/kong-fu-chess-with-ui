#show the moves history
class MovesLogRenderer:
    """
    Draws the move history.
    """

    def __init__(self, moves_log):
        self._moves_log = moves_log

    def render(self, canvas, snapshot=None):

        moves = self._moves_log.get_moves()
        
        #place:
        x = 450
        y = 30

        max_moves = 10 #show only 10 noves

        recent_moves = moves[-max_moves:]

        for move in recent_moves:

            canvas.put_text(
                move,
                x,
                y,
                0.45 #font size
            )

            y += 18