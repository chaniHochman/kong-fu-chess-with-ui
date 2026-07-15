"""
מחלקה האחראית על ניהול אנימציה של מצב אחד של כלי.

המחלקה אינה מציירת דבר.
תפקידה היחיד הוא לבחור בכל רגע את התמונה (Frame)
שיש להציג לפי הזמן שעבר מאז תחילת האנימציה.
"""

import time

class Animation:

    """
    יוצר אנימציה חדשה.

    frames : list[Img]
        רשימת כל התמונות של האנימציה.

    frames_per_sec : int
        מספר הפריימים לשנייה.

    is_loop : bool
        האם האנימציה חוזרת מההתחלה כאשר מגיעים לסופה.
    """

    def __init__(self, frames, frames_per_sec, is_loop):

        self.frames = frames
        self.frames_per_sec = frames_per_sec
        self.is_loop = is_loop

        # זמן תחילת האנימציה
        self.started_at = time.time()


    """
    מפעיל מחדש את האנימציה.

    משתמשים בפונקציה זו כאשר כלי מחליף State
    (לדוגמה מ-idle ל-move).
    """

    def restart(self):

        self.started_at = time.time()
    """
    מחזיר את התמונה (Frame) המתאימה לזמן הנוכחי.

    Returns
    -------
    Img
        אובייקט Img המכיל את התמונה שיש לצייר.
    """
    def get_current_frame(self):

        if not self.frames:
            return None

        elapsed = time.time() - self.started_at

        frame_duration = 1 / self.frames_per_sec

        frame_index = int(elapsed / frame_duration)

        if self.is_loop:
            frame_index %= len(self.frames)
        else:
            frame_index = min(frame_index,
                              len(self.frames) - 1)

        return self.frames[frame_index]
