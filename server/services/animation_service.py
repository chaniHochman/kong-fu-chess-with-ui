#מודיעה ללקוח איזו אנימציה להפעיל
class AnimationService:
    """
    Controls game animations.
    """

    def __init__(self):
        """
        Initialize animation service.
        """

        pass


    def handle_event(self, event):
        """
        React to animation events.
        """

        if event.type == EventType.GAME_STARTED:

            print("Start animation")