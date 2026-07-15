"""
Global configuration for the View layer.
All constants that are shared by the graphical system appear here.
"""

from pathlib import Path

# Board size
BOARD_ROWS = 8
BOARD_COLS = 8

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Animation timing
FRAME_DELAY_MS = 30
MAX_DT_MS = 100

# Assets
ASSETS_ROOT = Path("UI") / "assets" / "pieces1"

# Piece types (same names as model.Piece.kind)
PIECE_KINDS = (
    "pawn",
    "rook",
    "knight",
    "bishop",
    "queen",
    "king",
)

# Piece colors (same names as model.Piece.color)
PIECE_COLORS = (
    "white",
    "black",
)

# Visual animation states
ANIMATION_STATES = (
    "idle",
    "move",
    "jump",
    "short_rest",
    "long_rest",
)