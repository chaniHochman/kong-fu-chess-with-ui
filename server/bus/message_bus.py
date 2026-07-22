from collections import defaultdict


class MessageBus:
    """
    Central communication system.

    Components publish events.

    Components subscribe to events.

    Components never know each other directly.
    """

    # Create empty subscribers dictionary.
    def __init__(self):

        self._subscribers = defaultdict(list)

    # Register event handler.
    def subscribe(self, event_type, handler):

        self._subscribers[event_type].append(handler)

    # Publish event to all subscribers.
    def publish(self, event):

        handlers = self._subscribers.get(event.type, [])

        for handler in handlers:
            handler(event)