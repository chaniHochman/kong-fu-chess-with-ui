import unittest

from model.board import Board
from model.piece import Piece
from model.position import Position


class BoardTests(unittest.TestCase):
    def setUp(self):
        Piece._used_ids.clear()
        self.board = Board(8, 8)
        self.white_rook = Piece(1, "white", "rook", Position(0, 0))

    def test_board_dimensions_are_inferred_correctly(self):
        self.assertEqual(self.board.rows, 8)
        self.assertEqual(self.board.cols, 8)

    def test_empty_cells_return_no_piece(self):
        self.assertIsNone(self.board.get_piece(Position(3, 3)))

    def test_occupied_cells_return_the_correct_piece(self):
        self.board.add_piece(self.white_rook, Position(0, 0))
        self.assertIs(self.board.get_piece(Position(0, 0)), self.white_rook)

    def test_adding_two_pieces_to_same_cell_fails(self):
        self.board.add_piece(self.white_rook, Position(0, 0))
        another_piece = Piece(2, "black", "rook", Position(1, 1))
        with self.assertRaises(ValueError):
            self.board.add_piece(another_piece, Position(0, 0))

    def test_move_piece_updates_source_and_destination(self):
        self.board.add_piece(self.white_rook, Position(0, 0))
        self.board.move_piece(Position(0, 0), Position(4, 4))
        self.assertIsNone(self.board.get_piece(Position(0, 0)))
        self.assertIs(self.board.get_piece(Position(4, 4)), self.white_rook)
        self.assertEqual(self.white_rook.cell, Position(4, 4))

    def test_remove_piece_clears_the_cell(self):
        self.board.add_piece(self.white_rook, Position(0, 0))
        self.board.remove_piece(Position(0, 0))
        self.assertIsNone(self.board.get_piece(Position(0, 0)))

    def test_is_within_bounds_checks_board_limits(self):
        self.assertTrue(self.board.is_within_bounds(Position(0, 0)))
        self.assertTrue(self.board.is_within_bounds(Position(7, 7)))
        self.assertFalse(self.board.is_within_bounds(Position(-1, 0)))
        self.assertFalse(self.board.is_within_bounds(Position(8, 0)))


if __name__ == "__main__":
    unittest.main()
