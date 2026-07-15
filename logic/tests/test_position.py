import unittest

from model.position import Position


class PositionTests(unittest.TestCase):
    def test_equal_positions_with_same_row_and_col(self):
        self.assertEqual(Position(2, 4), Position(2, 4))

    def test_different_positions_are_not_equal(self):
        self.assertNotEqual(Position(2, 4), Position(3, 4))
        self.assertNotEqual(Position(2, 4), Position(2, 5))

    def test_repr_is_readable(self):
        self.assertEqual(repr(Position(2, 4)), "Position(row=2, col=4)")

    def test_invalid_row_and_col_raise_readable_errors(self):
        with self.assertRaisesRegex(TypeError, "row"):
            Position("2", 4)

        with self.assertRaisesRegex(TypeError, "col"):
            Position(2, "4")


if __name__ == "__main__":
    unittest.main()
