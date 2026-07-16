class Controller:

    def __init__(self, game_engine, board_mapper):
        self._game_engine = game_engine
        self._board_mapper = board_mapper
        self._selected = None


    # פעולה שמגיעה מהעכבר דרך CommandSender
    def on_click(self, position):

        # קליק ראשון - בחירת כלי
        if self._selected is None:
            piece = self._game_engine.get_piece(position)

            if piece is not None:
                self._selected = position
            return None


        # קליק שני - ניסיון תנועה
        result = self._game_engine.request_move(
            self._selected,
            position
        )

        self._selected = None

        return result