from view.protocols import Renderer



class ScoreRenderer:
    """
    Draws scores on the screen.
    """


    def __init__(
            self,
            score_data,
            x=20,
            y=30
    ):

        self._score_data = score_data

        self._x = x
        self._y = y



    def render(
            self,
            canvas,
            snapshot=None
    ):
        """
        Draw score on canvas.
        """


        scores = self._score_data.get_all_scores()



        canvas.put_text(
            f"White: {scores['white']}",
            self._x,
            self._y,
            0.8 #font size
        )


        canvas.put_text(
            f"Black: {scores['black']}",
            self._x,
            self._y + 35,
            0.8 #font size
        )