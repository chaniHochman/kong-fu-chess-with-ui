from logic.model.position import Position


class ClickCommand:
    """
    Represents a left-click command.
    """

    def __init__(self, position: Position):
        self.position = position

 
class JumpCommand:
    """
    Represents a jump command.
    """

    def __init__(self, position: Position):
        self.position = position