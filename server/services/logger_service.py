#רושמת אירועים ללוג
class LoggerService:
    """
    Handles logging of server events.
    """

    def __init__(self):
        """
        Initialize logger service.
        """

        pass


    def handle_event(self, event):
        """
        Save event information
        into the log.
        """

        print("LOG:", event)