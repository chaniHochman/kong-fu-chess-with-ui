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
        payload=None
    ):

        self.type = event_type

        self.payload = payload  #מידע נוסף