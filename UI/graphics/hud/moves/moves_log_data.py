#keep the moves history 
class MovesLogData:
    """
    Stores the history of all moves.
    """

    def __init__(self):
        self._moves = []

    def add_move(self, piece, source, destination):
        """
        Adds a move to the history.
        """

        move = (
            f"{piece.kind} "
            f"({source.row},{source.col})"
            f" -> "
            f"({destination.row},{destination.col})"
        )

        self._moves.append(move)

    def clear(self):
        """
        Clears the move history.
        """
        self._moves.clear()

    def get_moves(self):
        """
        Returns a copy of the move history.
        """
        return self._moves.copy()