# מתרגם פעולות משתמש (קליקים בפיקסלים) לפקודות למנוע המשחק
class Controller:
    # אתחול הבקר עם הפניות למנוע המשחק ולממיר קואורדינטות
    def __init__(self, game_engine, board_mapper):
        self._game_engine = game_engine
        self._board_mapper = board_mapper
        self._selected = None

    # טיפול בקליק פיקסלים: קליק ראשון בוחר כלי, קליק שני שולח בקשת מהלך למנוע
    # מחזיר את תוצאת הבקשה (MoveResult) כאשר מבוצע ניסיון תנועה
    def on_click(self, x: int, y: int):
        cell = self._board_mapper.pixel_to_cell(x, y)

        # קליק ראשון — בחירת כלי אם קיים
        if self._selected is None:
            if cell is None:
                return None
            self._selected = cell
            return None

        # קליק שני — ניסיון הזזה מהמיקום שנבחר ליעד
        if cell is None:
            self._selected = None
            return None

        result = self._game_engine.request_move(self._selected, cell)
        self._selected = None
        return result
