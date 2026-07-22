from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import cv2
import numpy as np
import pytest

from UI.graphics.animation.animation_library import AnimationLibrary
from UI.graphics.animation.piece_animator import PieceAnimator
from UI.graphics.board.board_geometry import BoardGeometry
from UI.graphics.board.board_loader import BoardLoader
from UI.graphics.board.board_renderer import BoardRenderer
from UI.graphics.display_manager import DisplayManager
from UI.graphics.img import Img
from UI.graphics.image_utils import ensure_alpha
from UI.graphics.input.commands import ClickCommand, JumpCommand
from UI.graphics.input.local_command_sender import LocalCommandSender
from UI.graphics.input.mouse_command_extractor import MouseCommandExtractor
from UI.graphics.pieces.piece_loader import PieceLoader
from UI.graphics.pieces.piece_renderer import PieceRenderer
from UI.graphics.hud.moves.moves_log_data import MovesLogData
from UI.graphics.hud.moves.moves_log_renderer import MovesLogRenderer
from UI.graphics.hud.score.score_data import ScoreData
from UI.graphics.hud.score.score_renderer import ScoreRenderer
from logic.model.position import Position


class FakeBoardMapper:
    def __init__(self, result):
        self.result = result

    def pixel_to_cell(self, x, y):
        return self.result


class FakeController:
    def __init__(self):
        self.clicked = []
        self.jumped = []

    def on_click(self, position):
        self.clicked.append(position)

    def on_jump(self, position):
        self.jumped.append(position)


class FakeGameEngine:
    def __init__(self):
        self.calls = 0

    def wait(self, dt):
        self.calls += 1

    def create_snapshot(self):
        return SimpleNamespace(pieces=[])

    def is_game_over(self):
        return self.calls >= 1


class FakeRenderer:
    def __init__(self):
        self.calls = []

    def render(self, canvas, snapshot):
        self.calls.append((canvas, snapshot))


def test_img_helpers_and_draw_operations(tmp_path):
    image_path = tmp_path / "sprite.png"
    image = np.zeros((8, 10, 3), dtype=np.uint8)
    cv2.imwrite(str(image_path), image)

    img = Img().read(image_path, size=(6, 6))
    assert img.width() == 6
    assert img.height() == 6

    blank = Img.create_blank(20, 20, channels=4)
    img.draw_on(blank, 2, 3)
    assert blank.img[3:9, 2:8].shape[0] == 6

    rgba_image = np.zeros((6, 6, 4), dtype=np.uint8)
    rgba_img = Img()
    rgba_img.img = rgba_image
    rgba_img.draw_on(blank, 0, 0)
    assert blank.img.shape[2] == 4

    copied = img.copy()
    assert copied.width() == img.width()

    img.put_text("hi", 1, 2, 1)
    assert img.img is not None

    with pytest.raises(ValueError):
        Img().draw_on(blank, 0, 0)


def test_ensure_alpha_converts_bgr_to_bgra():
    image = np.zeros((4, 4, 3), dtype=np.uint8)
    converted = ensure_alpha(image)
    assert converted.shape[2] == 4

    rgba_image = np.zeros((4, 4, 4), dtype=np.uint8)
    assert ensure_alpha(rgba_image).shape[2] == 4


def test_board_geometry_and_board_loader(tmp_path):
    geometry = BoardGeometry(window_width=320, window_height=240)
    assert geometry.cell_width == 40
    assert geometry.cell_height == 30

    position = Position(2, 3)
    x, y = geometry.cell_to_pixel(position)
    assert (x, y) == (120, 60)

    geometry.resize(400, 300)
    assert geometry.cell_width == 50
    assert geometry.cell_height == 37

    image_path = tmp_path / "board.png"
    cv2.imwrite(str(image_path), np.zeros((20, 20, 3), dtype=np.uint8))

    loader = BoardLoader(image_path, geometry)
    loader.load()
    board_image = loader.get_image()
    assert board_image is not None
    assert board_image.width() == 400
    assert board_image.height() == 300


def test_board_renderer_draws_background():
    class FakeBoardLoader:
        def get_image(self):
            return Img.create_blank(10, 10, channels=4)

    canvas = Img.create_blank(20, 20, channels=4)
    renderer = BoardRenderer(FakeBoardLoader())
    renderer.render(canvas, None)
    assert canvas.img.shape == (20, 20, 4)


def test_piece_loader_and_animation_library(tmp_path):
    assets_root = tmp_path / "assets"
    sprite_dir = assets_root / "PAWNWHITE" / "states" / "idle" / "sprites"
    sprite_dir.mkdir(parents=True)
    cv2.imwrite(str(sprite_dir / "1.png"), np.zeros((6, 6, 3), dtype=np.uint8))
    cv2.imwrite(str(sprite_dir / "2.png"), np.zeros((6, 6, 3), dtype=np.uint8))

    config_path = sprite_dir.parent / "config.json"
    config_path.write_text(json.dumps({
        "graphics": {"frames_per_sec": 10, "is_loop": False},
        "physics": {"next_state_when_finished": "move"},
    }))

    loader = PieceLoader(assets_root)
    assert loader.count_frames("pawn", "white", "idle") == 2

    first = loader.load_piece("pawn", "white", "idle", 1)
    second = loader.load_piece("pawn", "white", "idle", 1)
    assert first is second
    assert loader.load_config("pawn", "white", "idle")["graphics"]["frames_per_sec"] == 10

    library = AnimationLibrary(loader)
    library.load_animation("pawn", "white", "idle")
    assert library.get_frame("pawn", "white", "idle", 0) is not None
    assert library.count_frames("pawn", "white", "idle") == 2
    assert library.get_fps("pawn", "white", "idle") == 10
    assert library.is_loop("pawn", "white", "idle") is False
    assert library.get_next_state("pawn", "white", "idle") == "move"


def test_piece_animator_motion_and_frame_logic():
    animator = PieceAnimator()
    animator.start_motion("p1", 0, 0, 100, 50, 100)
    animator.update(50)
    assert animator.get_position("p1") == (50, 25)

    assert animator.get_position("missing") is None

    animator.start_motion("p2", 0, 0, 0, 0, 0)
    assert animator.get_position("p2") is None

    assert animator.get_frame_index("x", 4, 0, False) == 0
    assert animator.get_frame_index("x", 4, 20, False) == 1
    assert animator.get_frame_index("x", 4, 20, True) == 1

    animator.update(1000)
    assert animator.get_frame_index("x", 4, 20, False) == 3
    assert animator.get_frame_index("x", 4, 20, True) == 1


def test_piece_renderer_draws_from_snapshot():
    class FakeAnimationLibrary:
        def count_frames(self, kind, color, state):
            return 2

        def get_fps(self, kind, color, state):
            return 10

        def is_loop(self, kind, color, state):
            return False

        def get_frame(self, kind, color, state, frame_index):
            return Img.create_blank(4, 4, channels=4)

    canvas = Img.create_blank(100, 100, channels=4)
    geometry = BoardGeometry(window_width=100, window_height=100)
    animator = PieceAnimator()
    renderer = PieceRenderer(FakeAnimationLibrary(), animator, geometry)

    snapshot = SimpleNamespace(pieces=[SimpleNamespace(
        kind="pawn",
        color="white",
        state="idle",
        piece_id="p1",
        pixel_x=10,
        pixel_y=10,
    )])

    renderer.render(canvas, snapshot)
    assert canvas.img is not None


def test_score_and_moves_log_renderers():
    score_data = ScoreData()
    score_data.add_capture(SimpleNamespace(kind="pawn", color="white"))
    score_data.add_capture(SimpleNamespace(kind="queen", color="black"))

    score_renderer = ScoreRenderer(score_data, x=10, y=20)
    canvas = Img.create_blank(200, 200, channels=4)
    score_renderer.render(canvas, None)
    assert canvas.img is not None

    moves_log_data = MovesLogData()
    moves_log_data.add_move(SimpleNamespace(kind="pawn"), Position(1, 2), Position(2, 2))
    moves_log_data.add_move(SimpleNamespace(kind="rook"), Position(1, 1), Position(1, 8))
    moves_log_renderer = MovesLogRenderer(moves_log_data)
    moves_log_renderer.render(canvas, None)
    assert canvas.img is not None


def test_mouse_input_commands_and_local_sender():
    geometry = BoardGeometry(window_width=100, window_height=100)
    mapper = FakeBoardMapper(Position(1, 2))
    extractor = MouseCommandExtractor(mapper, geometry)

    left = extractor.extract_left_click(10, 20)
    right = extractor.extract_right_click(25, 35)
    assert isinstance(left, ClickCommand)
    assert isinstance(right, JumpCommand)
    assert left.position == Position(1, 2)
    assert right.position == Position(1, 2)

    mapper.result = None
    assert extractor.extract_left_click(10, 20) is None

    controller = FakeController()
    sender = LocalCommandSender(controller)
    sender.send(ClickCommand(Position(0, 0)))
    sender.send(JumpCommand(Position(1, 1)))
    assert controller.clicked[0] == Position(0, 0)
    assert controller.jumped[0] == Position(1, 1)


def test_display_manager_update_render_and_mouse_loop(monkeypatch):
    board_loader = SimpleNamespace(get_image=lambda: Img.create_blank(20, 20, channels=4))
    game_engine = FakeGameEngine()
    piece_animator = SimpleNamespace(update=lambda dt: None)
    mouse_extractor = SimpleNamespace(
        extract_left_click=lambda x, y: ClickCommand(Position(0, 0)),
        extract_right_click=lambda x, y: JumpCommand(Position(1, 1)),
    )
    command_sender = SimpleNamespace(send=lambda command: None)
    renderer_a = FakeRenderer()
    renderer_b = FakeRenderer()

    manager = DisplayManager(
        game_engine=game_engine,
        board_loader=board_loader,
        board_renderer=SimpleNamespace(render=lambda canvas, snapshot: None),
        piece_renderer=SimpleNamespace(render=lambda canvas, snapshot: None),
        piece_animator=piece_animator,
        score_renderer=renderer_a,
        moves_renderer=renderer_b,
        mouse_extractor=mouse_extractor,
        command_sender=command_sender,
    )

    manager.update()
    canvas = manager.render()
    assert canvas.width() == 20 + 350
    assert canvas.height() == 20

    manager._mouse_callback(cv2.EVENT_LBUTTONDOWN, 5, 5, 0, None)
    manager._mouse_callback(cv2.EVENT_RBUTTONDOWN, 5, 5, 0, None)

    monkeypatch.setattr(cv2, "namedWindow", lambda *args, **kwargs: None)
    monkeypatch.setattr(cv2, "setMouseCallback", lambda *args, **kwargs: None)
    monkeypatch.setattr(cv2, "imshow", lambda *args, **kwargs: None)
    monkeypatch.setattr(cv2, "waitKey", lambda *args, **kwargs: 27)
    monkeypatch.setattr(cv2, "destroyAllWindows", lambda: None)

    manager.run()
