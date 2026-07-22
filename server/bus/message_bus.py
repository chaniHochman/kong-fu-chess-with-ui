from collections import defaultdict


class MessageBus:
    """
    Central communication system of the server.

    Components can publish events
    and subscribe to events.

    Components do not know each other.
    """


    # Creates an empty event registry.
    def __init__(self):

        self._subscribers = defaultdict(list)



    # Registers a handler for a specific event type.
    def subscribe(
        self,
        event_type,
        handler
    ):

        self._subscribers[event_type].append(
            handler
        )



    # Publishes an event to all interested handlers.
    def publish(
        self,
        event
    ):

        handlers = self._subscribers.get(
            event.type,
            []
        )


        for handler in handlers:

            handler(event)