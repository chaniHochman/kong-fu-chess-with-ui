# תנועה (חלק כלי, מקו, יעד)
class Motion:
    def __init__(self, piece, source, target, is_jump=False):
        self.piece = piece
        self.source = source
        self.target = target
        self.is_jump = is_jump

        # קפיצה במקום נמשכת 1000 מ"ש; מהלך רגיל נמשך 1000 מ"ש לכל משבצת
        if is_jump or source == target:
            self.time_left = 1000
        else:
            distance = max(
                abs(target[0] - source[0]),
                abs(target[1] - source[1])
            )
            self.time_left = distance * 1000