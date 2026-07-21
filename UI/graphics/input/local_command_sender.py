#מתרגמת פקודה לקריאה למנוע
#כדי שהעכבר לא יכיר את GameEngine.
from UI.graphics.input.commands import ClickCommand, JumpCommand

class LocalCommandSender:

    def __init__(self, controller, game_engine=None):
        self._controller = controller
        self._game_engine = game_engine

    def send(self, command):

        if isinstance(command, ClickCommand):

            self._controller.on_click(
                command.position
            )

        elif isinstance(command, JumpCommand):

            if self._game_engine is not None:
                self._game_engine.request_jump(command.position)
            else:
                self._controller.on_jump(
                    command.position
                )