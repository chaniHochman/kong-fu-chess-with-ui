import unittest

from model.board import Board
from model.piece import Piece
from model.position import Position
from realtime.real_time_arbiter import RealTimeArbiter
from rules.rule_engine import MoveValidation, RuleEngine


class RuleEngineTests(unittest.TestCase):
    def setUp(self):
        Piece._used_ids.clear()
        self.board = Board(8, 8)
        self.engine = RuleEngine(self.board)

    def test_outside_board_is_rejected(self):
        validation = self.engine.validate_move(Position(0, 0), Position(8, 0))

        self.assertFalse(validation.is_valid)
        self.assertEqual(validation.reason, "outside_board")

    def test_empty_source_is_rejected(self):
        validation = self.engine.validate_move(Position(0, 0), Position(0, 1))

        self.assertFalse(validation.is_valid)
        self.assertEqual(validation.reason, "empty_source")

    def test_friendly_destination_is_rejected(self):
        white_rook = Piece(1, "white", "rook", Position(0, 0))
        self.board.add_piece(white_rook, Position(0, 0))
        self.board.add_piece(Piece(2, "white", "rook", Position(0, 1)), Position(0, 1))

        validation = self.engine.validate_move(Position(0, 0), Position(0, 1))

        self.assertFalse(validation.is_valid)
        self.assertEqual(validation.reason, "friendly_destination")

    def test_legal_rook_move_is_accepted(self):
        white_rook = Piece(1, "white", "rook", Position(0, 0))
        self.board.add_piece(white_rook, Position(0, 0))

        validation = self.engine.validate_move(Position(0, 0), Position(0, 3))

        self.assertTrue(validation.is_valid)
        self.assertEqual(validation.reason, "ok")

    def test_illegal_piece_move_is_rejected(self):
        white_pawn = Piece(1, "white", "pawn", Position(1, 1))
        self.board.add_piece(white_pawn, Position(1, 1))

        validation = self.engine.validate_move(Position(1, 1), Position(3, 1))

        self.assertFalse(validation.is_valid)
        self.assertEqual(validation.reason, "illegal_piece_move")

    def test_same_cell_jump_is_accepted_for_idle_piece(self):
        pawn = Piece(1, "white", "pawn", Position(1, 1))
        self.board.add_piece(pawn, Position(1, 1))

        validation = self.engine.validate_move(Position(1, 1), Position(1, 1))

        self.assertTrue(validation.is_valid)
        self.assertEqual(validation.reason, "jump")

    def test_same_cell_jump_is_rejected_for_non_idle_piece(self):
        pawn = Piece(1, "white", "pawn", Position(1, 1))
        pawn.state = "moving"
        self.board.add_piece(pawn, Position(1, 1))

        validation = self.engine.validate_move(Position(1, 1), Position(1, 1))

        self.assertFalse(validation.is_valid)
        self.assertEqual(validation.reason, "illegal_piece_move")


class RealTimeArbiterTests(unittest.TestCase):
    def setUp(self):
        Piece._used_ids.clear()
        self.board = Board(8, 8)
        self.arbiter = RealTimeArbiter(self.board)

    def test_jump_finishes_and_piece_remains_idle(self):
        pawn = Piece(1, "white", "pawn", Position(1, 1))
        self.board.add_piece(pawn, Position(1, 1))

        self.arbiter.start_motion(pawn, (1, 1), (1, 1))
        self.arbiter.advance_time(1000)

        self.assertIs(self.board.get_piece(Position(1, 1)), pawn)
        self.assertEqual(pawn.state, "idle")

    def test_airborne_piece_captures_arriving_enemy(self):
        jumping = Piece(1, "white", "rook", Position(0, 0))
        enemy = Piece(2, "black", "rook", Position(0, 1))
        self.board.add_piece(jumping, Position(0, 0))
        self.board.add_piece(enemy, Position(0, 1))

        self.arbiter.start_motion(jumping, (0, 0), (0, 0))
        self.arbiter.start_motion(enemy, (0, 1), (0, 0))
        self.arbiter.advance_time(1000)

        self.assertIs(self.board.get_piece(Position(0, 0)), jumping)
        self.assertIsNone(self.board.get_piece(Position(0, 1)))
        self.assertEqual(jumping.state, "idle")
        self.assertEqual(enemy.state, "captured")


if __name__ == "__main__":
    unittest.main()
