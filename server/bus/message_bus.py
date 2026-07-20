class MessageBus:
    """
    Implements internal server
    Publish / Subscribe communication.

    Publishers send events.
    Subscribers receive events
    they registered for.
    """


    # Initialize message bus.
    def __init__(self):

        self.subscribers = {}  #איזה פונקציות מאזינות לאיזה אירוע.



    # Register a handler for a specific event type.
    def subscribe(
        self,
        event_type,
        handler
    ):

        if event_type not in self.subscribers:

            self.subscribers[event_type] = []


        # Prevent duplicate registration.
        if handler not in self.subscribers[event_type]:

            self.subscribers[event_type].append(
                handler
            )


    #כשהשחקן יוצא
    # Remove a handler from a specific event type.
    def unsubscribe(
        self,
        event_type,
        handler
    ):

        if event_type not in self.subscribers:

            return


        if handler in self.subscribers[event_type]:

            self.subscribers[event_type].remove(
                handler
            )



    # Publish an event to all registered subscribers.
    def publish(
        self,
        event
    ):

        handlers = self.subscribers.get(
            event.type,
            []
        )


        for handler in handlers:

            handler(event)