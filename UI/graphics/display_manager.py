# הוא לא מצייר בעצמו.

# הוא רק אומר לכל אחד מתי לעבוד.isplayManager – חיבור הכול: לולאת המשחק, עדכון (update), ציור (render), קליטת עכבר והצגת המסך.




self.renderers = [
    board_renderer,
    piece_renderer,
    score_renderer
]
for renderer in self.renderers:
    renderer.render(canvas, snapshot)