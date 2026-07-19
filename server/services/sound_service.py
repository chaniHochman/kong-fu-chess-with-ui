#מודיעה ללקוח איזה צליל לנגן
class SoundService:
    """
    Sends sound notifications
    to clients.
    """

    def __init__(self):
        """
        Initialize sound service.
        """

        pass


    def handle_event(self, event):
        """
        React to game events
        by requesting sounds.
        """

        if event.type == EventType.MOVE_ACCEPTED:

            print("Play move sound")