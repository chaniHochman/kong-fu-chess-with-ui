from logic.realtime.motion import Motion
from logic.model.position import Position

# ניהול זמן ותנועות
class RealTimeArbiter:
    
    # אתחול המנהל: שומר הפניות ללוח ולמנוע המשחק
    def __init__(self, board, game_engine=None, piece_animator=None):
        self._board = board
        self._game_engine = game_engine
        self._piece_animator = piece_animator
        # רשימת תנועות פעילות
        self._active_motions = []
    
    # בודק האם קיימת תנועה פעילה ברשימה
    def has_active_motion(self):
        
        return len(self._active_motions) > 0
    

    # הוספת תנועה שכבר אושרה לרשימת התנועות הפעילות
    def start_motion(self, piece, source, target):
        
        is_jump = source == target
        motion = Motion(
            piece,
            source,
            target,
            is_jump=is_jump
        )
        piece.state = "jumping" if is_jump else "moving"
        # מכניס לרשימת תנועות פעילות
        self._active_motions.append(motion)
        if self._piece_animator:

            self._piece_animator.start_motion(
                id(piece),

                source[1] * CELL_SIZE,
                source[0] * CELL_SIZE,

                target[1] * CELL_SIZE,
                target[0] * CELL_SIZE,

                motion.time_left
            )
    # מקדם את הזמן המדומה ומסיים תנועות שהזמן שלהן תם
    def advance_time(self, ms):
       
        
        for motion in self._active_motions:
            motion.time_left -= ms

        finished = [motion for motion in self._active_motions if motion.time_left <= 0]
        finished.sort(key=lambda motion: motion.is_jump)

        for motion in finished:
            self._finish_motion(motion)#קריאה לפונקצית הוזזת חייל
            self._active_motions.remove(motion)#הסרה מרשימת הפקודות

    # מטפל בסיום קפיצה במקום: הכלי נותר באותו תא ונוחת חזרה
    def _finish_jump_motion(self, motion):
        source = motion.source
        src_pos = Position(source[0], source[1])
        piece = self._board.get_piece(src_pos)
        if piece is None:
            return
        piece.state = "idle"

    #הזזת כלי ממקור ליעד
    # סיום תנועה: מעדכן את הלוח בהתאם למקור וליעד
    def _finish_motion(self, motion):

        source = motion.source
        target = motion.target


        # אם זו קפיצה במקום, הכלי נוחת ומהלך זה מסתיים ללא הזזת מיקום
        if motion.is_jump:
            self._finish_jump_motion(motion)
            return

        # המרה ל-Position כדי להשתמש בממשק ה־Board
        src_pos = Position(source[0], source[1])
        tgt_pos = Position(target[0], target[1])

        # הכלי עדיין נמצא בתא המקור
        piece = self._board.get_piece(src_pos)
        if piece is None:
            return

        # אם כלי זה מגיע ליעד שבו יש כלי קופץ של היריב, כלי זה נתפס במהלך הנחיתה
        captured = self._board.get_piece(tgt_pos)
        if captured is not None and getattr(captured, "state", None) == "jumping" and captured.color != piece.color:
            self._board.remove_piece(src_pos)
            piece.state = "captured"
            if piece.kind == "king" and self._game_engine:
                self._game_engine.notify_king_captured()
            return

        # 1. הסרת הכלי מהמקור
        self._board.remove_piece(src_pos)

        # 2. בדיקה האם נאכל מלך (כלי מסוג 'king')
        if captured is not None and getattr(captured, "kind", None) == "king":
            if self._game_engine:
                self._game_engine.notify_king_captured()

        # 3. הסרת הכלי שביעד (אם קיים) ואז הצבת הכלי במיקום היעד
        if captured is not None:
            self._board.remove_piece(tgt_pos)

        # שימוש ב־add_piece מבצע גם בדיקות ומעדכן את מיקום הכלי
        try:
            self._board.add_piece(piece, tgt_pos)
        except Exception:
            self._board._grid[tgt_pos.row][tgt_pos.col] = piece
            piece.cell = tgt_pos
        piece.state = "idle"

        # קידום חייל (pawn) לשפרה (queen) אם הגיע לשורה האחרונה
        if piece is not None and getattr(piece, "kind", None) == "pawn":
            # לבן מקדם לשורה 0, שחור לשורה rows-1
            if piece.color == "white" and tgt_pos.row == 0:
                piece.kind = "queen"
            if piece.color == "black" and tgt_pos.row == self._board.rows - 1:
                piece.kind = "queen"