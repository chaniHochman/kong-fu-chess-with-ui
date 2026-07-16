from pathlib import Path
import pathlib
import sys


sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parent)
)


from logic.input_output.BoardParser import BoardParser

from logic.rules.rule_engine import RuleEngine
from logic.realtime.real_time_arbiter import RealTimeArbiter
from logic.engine.game_engine import GameEngine

from logic.input.board_mapper import BoardMapper
from logic.input.controller import Controller
from logic.input.board_mapper import CELL_SIZE

from UI.graphics.display_manager import DisplayManager
from UI.graphics.board.board_geometry import BoardGeometry

from UI.graphics.board.board_loader import BoardLoader
from UI.graphics.board.board_renderer import BoardRenderer

from UI.graphics.pieces.piece_renderer import PieceRenderer
from UI.graphics.animation.piece_animator import PieceAnimator
from UI.graphics.animation.animation_library import AnimationLibrary
from UI.graphics.pieces.piece_loader import PieceLoader


from UI.graphics.input.mouse_command_extractor import MouseCommandExtractor
from UI.graphics.input.local_command_sender import LocalCommandSender



def build_game():

    #loade board

    parser = BoardParser()

    board = parser.parse_to_board(
        """
        bR bN bB bQ bK bB bN bR
        bP bP bP bP bP bP bP bP
        .  .  .  .  .  .  .  .
        .  .  .  .  .  .  .  .
        .  .  .  .  .  .  .  .
        .  .  .  .  .  .  .  .
        wP wP wP wP wP wP wP wP
        wR wN wB wQ wK wB wN wR
        """
    )

    rule_engine = RuleEngine(board)

    #animation

    piece_animator = PieceAnimator()


    # RealTimeArbiter
    
    arbiter = RealTimeArbiter(
        board,
        piece_animator=piece_animator
    )


    engine = GameEngine(
        board,
        rule_engine,
        arbiter
    )


    arbiter._game_engine = engine


    mapper = BoardMapper(
        board.rows,
        board.cols
    )

    controller = Controller(
        engine,
        mapper
    )

    # View

    geometry = BoardGeometry()


    mouse_extractor = MouseCommandExtractor(
        mapper,
        geometry
    )

    command_sender = LocalCommandSender(
        controller,
        engine
    )



    # טעינת תמונות כלים

    piece_loader = PieceLoader(Path("UI/assets/pieces1"))


    animation_library = AnimationLibrary(
        piece_loader
    )

    for kind in ("K", "Q", "R", "B", "N", "P"):
        for color in ("W", "B"):
            for state in ("idle", "move", "jump", "short_rest", "long_rest"):
                animation_library.load_animation(kind, color, state)


    piece_renderer = PieceRenderer(
        animation_library,
        piece_animator
    )



    board_loader = BoardLoader(Path("UI/assets/board.png"), geometry)
    board_loader.load()


    board_renderer = BoardRenderer(board_loader)



    display = DisplayManager(

        engine,

        board_loader,

        board_renderer,

        piece_renderer,

        piece_animator,

        None,

        None,

        mouse_extractor,

        command_sender

    )

    return display


def main():

    display = build_game()

    display.run()

if __name__ == "__main__":
    main()