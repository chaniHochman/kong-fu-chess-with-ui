#מעדכנת דירוג ELO
class ScoreService:
    """
    Updates player ratings.
    """

    def __init__(self):
        """
        Initialize score service.
        """
        pass


    def handle_event(self, event):
        """
        Update ratings
        after game ends.
        """

        if event.type == EventType.GAME_ENDED:

            print("Updating ELO...")