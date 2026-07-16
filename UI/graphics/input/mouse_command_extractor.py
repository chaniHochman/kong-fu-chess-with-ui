#מקבלת פיקסל ומחזירה מיקום
from UI.graphics.input.commands import (
    ClickCommand,
    JumpCommand
)


class MouseCommandExtractor:

    """
    Converts mouse clicks
    into commands.
    """
    def __init__(
            self,
            board_mapper,
            geometry
    ):

        self._board_mapper = board_mapper
        self._geometry = geometry


    def extract_left_click(
            self,
            x,
            y
    ):
       #to move acording to the board 
        x -= self._geometry.board_origin_x
        y -= self._geometry.board_origin_y

        position = self._board_mapper.pixel_to_cell(
            x,
            y
        )

        if position is None:
            return None

        return ClickCommand(position)


    def extract_right_click(
            self,
            x,
            y
    ):
        #to move acording to the board 
        x -= self._geometry.board_origin_x
        y -= self._geometry.board_origin_y

        position = self._board_mapper.pixel_to_cell(
            x,
            y
        )

        if position is None:
            return None

        return JumpCommand(position)