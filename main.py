
import sys
import pathlib

# ודא שספריית הפרויקט נמצאת ב־sys.path כדי שניתן יהיה לייבא חבילות מקומיות
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from input.board_mapper import BoardMapper
from input.controller import Controller
from input_output.BoardParser import BoardParser
from input_output.board_printer import BoardPrinter
from rules.rule_engine import RuleEngine
from realtime.real_time_arbiter import RealTimeArbiter
from engine.game_engine import GameEngine


# קורא את בלוק ה"Board:" ובלוק ה"Commands:" מתוך stdin
def read_board_and_commands():
    lines = sys.stdin.read().splitlines()
    reading_board = False
    reading_commands = False
    board_lines = []
    commands = []

    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s == "Board:":
            reading_board = True
            reading_commands = False
            continue
        if s == "Commands:":
            reading_board = False
            reading_commands = True
            continue
        if reading_board:
            board_lines.append(line.rstrip())
        elif reading_commands:
            commands.append(s)

    return "\n".join(board_lines), commands


# בניית רכיבי המשחק: לוח, מנוע חוקים, ארביטר זמן, מנוע משחק ובקר
def build_game_from_text(board_text):
    parser = BoardParser()
    # השתמש ב־Board מלא ולא במטריצה כדי שאובייקטים כמו RuleEngine/Arbiter יעבדו
    board = parser.parse_to_board(board_text)

    rule_engine = RuleEngine(board)
    arbiter = RealTimeArbiter(board)
    engine = GameEngine(board, rule_engine, arbiter)
    # קישור מעגלי: הארביטר צריך לשלח התראות למנוע
    arbiter._game_engine = engine

    mapper = BoardMapper(board.rows, board.cols)
    controller = Controller(engine, mapper)

    return board, engine, controller


# מעבד פקודות מסוג `move X Y` (פיקסלים) ומשתמש ב־`Controller.on_click`
def process_commands(board, engine, controller, commands):
    """תומך בפקודות:
    - click X Y  : קליק פיקסלים (בחר/הזז)
    - wait N      : קדם זמן ב־N מילישניות
    - print board : הדפס את הלוח הנוכחי
    """
    printer = BoardPrinter(board)

    for cmd in commands:
        parts = cmd.split()
        if not parts:
            continue
        op = parts[0].lower()

        if op == "click" and len(parts) == 3:
            try:
                x = int(parts[1])
                y = int(parts[2])
            except ValueError:
                continue   
            result = controller.on_click(x, y)
            # # אפשר להדפיס תוצאת מהלך אם רוצים
            # if result is not None and not result.success:
            #     # שגיאות חוקיות מדווחות כ־MoveResult
            #     print(f"MoveResult: {result}")

        elif op == "wait" and len(parts) == 2:
            try:
                ms = int(parts[1])
            except ValueError:
                continue
            # engine.wait מקדם את הארביטר בזמן מדומה
            engine.wait(ms)

        elif op == "print" and len(parts) >= 2 and parts[1].lower() == "board":
            printer.print_board()

        # אפשרות לשמור פקודה move X Y להתאמה לאמצעים קודמים
        elif op == "move" and len(parts) == 3:
            try:
                x = int(parts[1])
                y = int(parts[2])
            except ValueError:
                continue
            controller.on_click(x, y)

        else:
            # פקודה לא מוכרת — מתעלמים
            continue


def main():

    board_text, commands = read_board_and_commands()
    if not board_text:
        print("No board input detected.")
        return

    board, engine, controller = build_game_from_text(board_text)

    # עיבוד פקודות (click/wait/print)
    process_commands(board, engine, controller, commands)

    # draw_board(board, size=(800, 800), board_path="assets/board.png")

if __name__ == "__main__":
    main()


