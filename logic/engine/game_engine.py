from model.move_result import MoveResult
from rules.rule_engine import RuleEngine

# מנהל לוגיקה של משחק: מקבל מצב לוח, בודק מהלכים ומפעיל תנועות
class GameEngine:
    # יוזם את המנוע עם אובייקט לוח, מנוע חוק וארביטר לזמן
    def __init__(self, board, rule_engine: RuleEngine, real_time_arbiter):
        self._board = board
        self._rule_engine = rule_engine
        self._real_time_arbiter = real_time_arbiter
        self._game_over = False

    # מחזיר האם המשחק נגמר
    def is_game_over(self):
        return self._game_over

    # בקשת מהלך מהמיקום source ליעד target (Positions)
    def request_move(self, source, target):
        # אם המשחק כבר הסתיים — אין לבצע מהלכים
        if self._game_over:
            return MoveResult(False, "game_over")

        # כלי יכול לקפוץ אפילו כאשר קיימות תנועות אחרות;
        # כל כלי חייב להיות במצב idle לפני שיזוז או יקפוץ
        piece = self._board.get_piece(source)
        if piece is not None and piece.state != "idle":
            return MoveResult(False, "piece_busy")

        validation = self._rule_engine.validate_move(source, target)
        # validation הוא MoveValidation
        if not validation.is_valid:
            return MoveResult(False, validation.reason)

        # אם חוקי — בקש מהארביטר להתחיל תנועה
        piece = self._board.get_piece(source)
        if piece is None:
            return MoveResult(False, "empty_source")

        # הארביטר עובד עם תיאורים לוגיים (row,col)
        self._real_time_arbiter.start_motion(piece, (source.row, source.col), (target.row, target.col))
        return MoveResult(True, "ok")

    # מקדם זמן מדומה
    def wait(self, ms):
        self._real_time_arbiter.advance_time(ms)

    # נקרא כאשר המלך נאסר
    def notify_king_captured(self):
        self._game_over = True