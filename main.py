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


from view.display_manager import DisplayManager
from view.geometry import BoardGeometry

from view.board_loader import BoardLoader
from view.board_renderer import BoardRenderer

from view.pieces.piece_renderer import PieceRenderer
from view.pieces.piece_animator import PieceAnimator
from view.pieces.animation_library import AnimationLibrary
from view.pieces.piece_loader import PieceLoader


from view.input.mouse_command_extractor import MouseCommandExtractor
from view.input.local_command_sender import LocalCommandSender



def build_game():

    #loade board

    parser = BoardParser()
    
    board = parser.parse_to_board(
        """
        KW......KB
        .........
        .........
        .........
        .........
        .........
        .........
        QW......QB
        """
    )



    # ==========================
    # 2. מנוע חוקים
    # ==========================

    rule_engine = RuleEngine(board)



    # ==========================
    # 3. אנימציה
    # ==========================

    piece_animator = PieceAnimator()



    # ==========================
    # 4. RealTimeArbiter
    # ==========================

    arbiter = RealTimeArbiter(
        board,
        piece_animator
    )



    # ==========================
    # 5. GameEngine
    # ==========================

    engine = GameEngine(
        board,
        rule_engine,
        arbiter
    )


    arbiter._game_engine = engine



    # ==========================
    # 6. Controller
    # ==========================

    mapper = BoardMapper(
        board.rows,
        board.cols
    )


    controller = Controller(
        engine,
        mapper
    )



    # ==========================
    # 7. View
    # ==========================


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

    piece_loader = PieceLoader()


    animation_library = AnimationLibrary(
        piece_loader
    )


    piece_renderer = PieceRenderer(
        animation_library,
        piece_animator
    )



    board_loader = BoardLoader()



    board_renderer = BoardRenderer()



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