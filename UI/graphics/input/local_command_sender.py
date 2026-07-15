#מתרגמת פקודה לקריאה למנוע
#כדי שהעכבר לא יכיר את GameEngine.
class LocalCommandSender:

    def __init__(
            self,
            controller,
            game_engine
    ):
        self._controller = controller
        self._game_engine = game_engine


    def send(self, command):

        if isinstance(command, ClickCommand):

            self._controller.handle_click(
                command.position
            )

        elif isinstance(command, JumpCommand):

            self._game_engine.request_jump(
                command.position
            )