# זו אחת המחלקות החשובות ביותר.

#מחלקה אחת שמחשבת את מיקום וגודל התאים.

from dataclasses import dataclass

import UI.graphics.config as config
from model.position import Position 


@dataclass
class BoardGeometry:
    """
    Converts between board coordinates and pixel coordinates.
    """

    rows: int = config.BOARD_ROWS
    cols: int = config.BOARD_COLS

    window_width: int = config.WINDOW_WIDTH
    window_height: int = config.WINDOW_HEIGHT

    board_origin_x: int = 0
    board_origin_y: int = 0

    @property
    def cell_width(self) -> int:
        return self.window_width // self.cols

    @property
    def cell_height(self) -> int:
        return self.window_height // self.rows

    def cell_to_pixel(self, position: Position) -> tuple[int, int]:
        """
        Returns the upper-left pixel of a board cell.
        """

        x = self.board_origin_x + position.col * self.cell_width
        y = self.board_origin_y + position.row * self.cell_height

        return x, y  #return the num s of pixels

    def resize(self, width: int, height: int):
        """
        Updates window size after resizing.
        """

        self.window_width = width
        self.window_height = height