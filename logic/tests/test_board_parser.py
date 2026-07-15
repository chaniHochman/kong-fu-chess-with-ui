import unittest

from input_output.BoardParser import BoardParser


class BoardParserTests(unittest.TestCase):
    def test_read_board_creates_matrix_from_text(self):
        text = "wR .\n. bP"
        parser = BoardParser()
        board = parser.parse_board(text)
        # board = BoardParser.read_board(text)

        self.assertEqual(board, [["wR", "."], [".", "bP"]])


if __name__ == "__main__":
    unittest.main()
