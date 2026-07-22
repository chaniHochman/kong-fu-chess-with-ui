class Event:
    """
    Represents an internal server event.

    Events are transferred through
    MessageBus between server components.
    """


    # Create a new event.
    def __init__(
        self,
        event_type,
        data=None
    ):

        self.type = event_type

        self.data = data or {} #מידע נוסף