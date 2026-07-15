#keep the score
class ScoreData:
    """
    Stores game scores.

    Does not know anything about graphics.
    """
    VALUES = {
        "pawn": 1,
        "knight": 3,
        "bishop": 3,
        "rook": 5,
        "queen": 9,
        "king": 100
    }

    def __init__(self):

        self._scores = {
            "white": 0,
            "black": 0
        }



    def add_capture(self, piece):
        """
        Adds score after capturing a piece.
        """


        if piece is None:
            return


        value = self.VALUES.get(
            piece.kind,
            0
        )
        # מי שתפס את הכלי
        # מקבל את הניקוד

        if piece.color == "white":

            self._scores["black"] += value

        else:

            self._scores["white"] += value



    def get_score(self, color):

        return self._scores[color]



    def get_all_scores(self):

        return self._scores.copy()