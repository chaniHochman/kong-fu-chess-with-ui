import unittest

from model.piece import Piece
from model.position import Position


class PieceTests(unittest.TestCase):
    def setUp(self):
        Piece._used_ids.clear()

    def test_piece_stores_core_attributes(self):
        piece = Piece(id=1, color="white", kind="pawn", cell=Position(1, 0))

        self.assertEqual(piece.id, 1)
        self.assertEqual(piece.color, "white")
        self.assertEqual(piece.kind, "pawn")
        self.assertEqual(piece.cell, Position(1, 0))
        self.assertEqual(piece.state, "idle")

    def test_duplicate_ids_are_rejected(self):
        Piece(id=10, color="white", kind="king", cell=Position(0, 4))

        with self.assertRaisesRegex(ValueError, "unique"):
            Piece(id=10, color="black", kind="queen", cell=Position(7, 4))

    def test_invalid_values_raise_errors(self):
        with self.assertRaisesRegex(ValueError, "color"):
            Piece(id=2, color="yellow", kind="pawn", cell=Position(1, 1))

        with self.assertRaisesRegex(ValueError, "kind"):
            Piece(id=3, color="black", kind="superman", cell=Position(1, 1))

        with self.assertRaisesRegex(ValueError, "state"):
            Piece(id=4, color="black", kind="rook", cell=Position(1, 1), state="frozen")

    def test_cell_must_be_a_position(self):
        with self.assertRaisesRegex(TypeError, "cell"):
            Piece(id=5, color="white", kind="bishop", cell=(1, 1))

    def test_repr_is_readable(self):
        piece = Piece(id=6, color="black", kind="knight", cell=Position(2, 3))
        self.assertEqual(repr(piece), "Piece(id=6, color='black', kind='knight', cell=Position(row=2, col=3), state='idle')")


if __name__ == "__main__":
    unittest.main()
