#מתרגמת פקודה לקריאה למנוע
#כדי שהעכבר לא יכיר את GameEngine.
from UI.graphics.input.commands import ClickCommand, JumpCommand

class LocalCommandSender:

    def __init__(self, controller):
        self._controller = controller


    def send(self, command):

        if isinstance(command, ClickCommand):

            self._controller.on_click(
                command.position
            )

        elif isinstance(command, JumpCommand):

            self._controller.on_jump(
                command.position
            )