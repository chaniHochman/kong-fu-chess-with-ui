from logic.model.piece import Piece
from logic.model.position import Position


def is_legal_piece_move(piece: Piece, source: Position, destination: Position) -> bool:
    """בדוק אם מהלך של כלי נתון הוא חוקי מבחינת כלל התנועה שלו."""
    if not isinstance(piece, Piece):
        raise TypeError("piece must be a Piece")
    if not isinstance(source, Position):
        raise TypeError("source must be a Position")
    if not isinstance(destination, Position):
        raise TypeError("destination must be a Position")

    delta_row = destination.row - source.row
    delta_col = destination.col - source.col
    abs_row = abs(delta_row)
    abs_col = abs(delta_col)

    if piece.kind == "rook":
        return (delta_row == 0 and delta_col != 0) or (delta_row != 0 and delta_col == 0)

    if piece.kind == "bishop":
        return abs_row == abs_col and abs_row != 0

    if piece.kind == "queen":
        return (abs_row == abs_col and abs_row != 0) or (delta_row == 0 and delta_col != 0) or (delta_row != 0 and delta_col == 0)

    if piece.kind == "knight":
        return {abs_row, abs_col} in [{1, 2}, {2, 1}]

    if piece.kind == "king":
        return max(abs_row, abs_col) == 1

    if piece.kind == "pawn":
        if piece.color == "white":
            forward = -1
        else:
            forward = 1
        return delta_col == 0 and delta_row == forward

    raise ValueError(f"unsupported piece kind: {piece.kind}")
