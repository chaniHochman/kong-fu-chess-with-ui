from dataclasses import dataclass

from logic.model.position import Position
from logic.rules.piece_rules import is_legal_piece_move


@dataclass
class MoveValidation:
    is_valid: bool  #האם הצעד חוקי
    reason: str  #סיבה אם הצעד לא חוקי


class RuleEngine:
    """מאמת מהלכים על לוח שחמט ללא שינוי מצב המשחק."""

    def __init__(self, board):
        self.board = board

    def validate_move(self,source: Position, destination: Position) -> MoveValidation:
        """בודק אם מהלך מהתא source אל destination חוקי."""
        if not isinstance(source, Position):
            raise TypeError("source must be a Position")
        if not isinstance(destination, Position):
            raise TypeError("destination must be a Position")

        if not self.board.is_within_bounds(source) or not self.board.is_within_bounds(destination):
            return MoveValidation(is_valid=False, reason="outside_board")

        piece = self.board.get_piece(source)
        if piece is None:
            return MoveValidation(is_valid=False, reason="empty_source")

        destination_piece = self.board.get_piece(destination)
        if source == destination:
            if piece.state != "idle":
                return MoveValidation(is_valid=False, reason="illegal_piece_move")
            return MoveValidation(is_valid=True, reason="jump")

        if destination_piece is not None and destination_piece.color == piece.color:
            return MoveValidation(is_valid=False, reason="friendly_destination")

        if piece.kind == "pawn":
            return self._is_pawn_move_legal(piece, source, destination, destination_piece)

        if is_legal_piece_move(piece, source, destination):
            if piece.kind in {"rook", "bishop", "queen"}:
                if not self._is_path_clear(source, destination):
                    return MoveValidation(is_valid=False, reason="path_blocked")
            return MoveValidation(is_valid=True, reason="ok")

        return MoveValidation(is_valid=False, reason="illegal_piece_move")

#מחזיר אמת אם המהלך הוא ישר או אלכסוני, אחרת שקר
    def _is_straight_or_diagonal_move(self, source: Position, destination: Position) -> bool:
        delta_row = destination.row - source.row
        delta_col = destination.col - source.col
        abs_row = abs(delta_row)
        abs_col = abs(delta_col)

        return (
            (delta_row == 0 and delta_col != 0)
            or (delta_col == 0 and delta_row != 0)
            or (abs_row == abs_col and abs_row != 0)
        )

#בדיקה האם הדרך מהמקור ליעד פנויה מכלי אחר (למעט המקור והיעד עצמם)

    def _is_path_clear(self, source: Position, destination: Position) -> bool:
        if source == destination:
            return True

        if not self._is_straight_or_diagonal_move(source, destination):
            return False

        row_step = 0 if destination.row == source.row else (1 if destination.row > source.row else -1)
        col_step = 0 if destination.col == source.col else (1 if destination.col > source.col else -1)

        current_row = source.row + row_step
        current_col = source.col + col_step
        while current_row != destination.row or current_col != destination.col:
            current_position = Position(current_row, current_col)
            if self.board.get_piece(current_position) is not None:
                return False
            current_row += row_step
            current_col += col_step

        return True
#בדיקה האם מהלך של חייל (pawn) חוקי, כולל תנועה קדימה, קפיצה והתקפה אלכסונית    
    def _is_pawn_move_legal(self, piece, source: Position, destination: Position, destination_piece) -> MoveValidation:
        delta_row = destination.row - source.row
        delta_col = destination.col - source.col

        forward = -1 if piece.color == "white" else 1
        start_row = 6 if piece.color == "white" else 1

        if delta_col == 0 and delta_row == forward:
            if destination_piece is None:
                return MoveValidation(is_valid=True, reason="ok")
            return MoveValidation(is_valid=False, reason="destination_occupied")

        if delta_col == 0 and delta_row == 2 * forward:
            if source.row != start_row:
                return MoveValidation(is_valid=False, reason="illegal_piece_move")
            middle_position = Position(source.row + forward, source.col)
            if self.board.get_piece(middle_position) is not None:
                return MoveValidation(is_valid=False, reason="path_blocked")
            if destination_piece is not None:
                return MoveValidation(is_valid=False, reason="destination_occupied")
            return MoveValidation(is_valid=True, reason="ok")

        if abs(delta_col) == 1 and delta_row == forward and destination_piece is not None:
            return MoveValidation(is_valid=True, reason="ok")

        return MoveValidation(is_valid=False, reason="illegal_piece_move")
