import unittest
from unittest.mock import MagicMock
from model.position import Position
from model.game_snapshot import GameSnapshot, PieceSnapshot
from input.board_mapper import BoardMapper
from input.controller import Controller
from view.renderer import Renderer


class TestBoardMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = BoardMapper(8, 8)

    def test_pixel_to_cell_top_left(self):
        pos = self.mapper.pixel_to_cell(50, 50)
        self.assertEqual(pos, Position(0, 0))

    def test_pixel_to_cell_second_col(self):
        pos = self.mapper.pixel_to_cell(150, 50)
        self.assertEqual(pos, Position(0, 1))

    def test_pixel_to_cell_second_row(self):
        pos = self.mapper.pixel_to_cell(50, 150)
        self.assertEqual(pos, Position(1, 0))

    def test_pixel_outside_board_returns_none(self):
        pos = self.mapper.pixel_to_cell(900, 900)
        self.assertIsNone(pos)

    def test_pixel_negative_returns_none(self):
        pos = self.mapper.pixel_to_cell(-1, 50)
        self.assertIsNone(pos)


class TestController(unittest.TestCase):

    def setUp(self):
        self.engine = MagicMock()
        self.mapper = BoardMapper(8, 8)
        self.ctrl = Controller(self.engine, self.mapper)

    def test_first_click_inside_selects(self):
        self.ctrl.on_click(50, 50)
        self.assertEqual(self.ctrl._selected, Position(0, 0))

    def test_first_click_outside_ignored(self):
        self.ctrl.on_click(900, 900)
        self.assertIsNone(self.ctrl._selected)

    def test_second_click_inside_sends_move_and_clears(self):
        self.ctrl.on_click(50, 50)
        self.ctrl.on_click(150, 50)
        self.engine.request_move.assert_called_once_with(Position(0, 0), Position(0, 1))
        self.assertIsNone(self.ctrl._selected)

    def test_second_click_outside_cancels_selection(self):
        self.ctrl.on_click(50, 50)
        self.ctrl.on_click(900, 900)
        self.assertIsNone(self.ctrl._selected)
        self.engine.request_move.assert_not_called()


class TestRenderer(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock()
        self.renderer = Renderer(self.view)

    def _make_snapshot(self, pieces=None, selected_cell=None, game_over=False):
        return GameSnapshot(8, 8, pieces or [], selected_cell, game_over)

    def test_render_draws_grid(self):
        self.renderer.render(self._make_snapshot())
        self.assertEqual(self.view.draw_cell.call_count, 64)

    def test_render_draws_piece(self):
        p = PieceSnapshot("pawn", "white", 50, 50, "idle")
        self.renderer.render(self._make_snapshot(pieces=[p]))
        self.view.draw_piece.assert_called_once_with("pawn", "white", 50, 50, False)

    def test_captured_piece_not_drawn(self):
        p = PieceSnapshot("pawn", "white", 50, 50, "captured")
        self.renderer.render(self._make_snapshot(pieces=[p]))
        self.view.draw_piece.assert_not_called()

    def test_selected_piece_highlighted(self):
        p = PieceSnapshot("pawn", "white", 0, 0, "idle")
        snap = self._make_snapshot(pieces=[p], selected_cell=Position(0, 0))
        self.renderer.render(snap)
        self.view.draw_piece.assert_called_once_with("pawn", "white", 0, 0, True)

    def test_game_over_shows_message(self):
        self.renderer.render(self._make_snapshot(game_over=True))
        self.view.draw_message.assert_called_once_with("Game Over")

    def test_no_game_over_no_message(self):
        self.renderer.render(self._make_snapshot(game_over=False))
        self.view.draw_message.assert_not_called()


if __name__ == "__main__":
    unittest.main()
