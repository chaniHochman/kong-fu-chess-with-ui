# זה ערוץ התקשורת הפנימי של השרת.
# שמחלקות לא ידברו ישירות אחת עם השנייה.

class MessageBus:
    """
    Implements Publish/Subscribe
    message bus.
    """

    def __init__(self):
        """
        Initialize subscribers list.
        """

        self.subscribers = {}



    def subscribe(self, event_type, handler):
        """
        Register handler
        for specific event type.
        """

        if event_type not in self.subscribers:

            self.subscribers[event_type] = []

        self.subscribers[event_type].append(handler)



    def publish(self, event):
        """
        Publish event
        to all subscribers.
        """

        handlers = self.subscribers.get(
            event.type,
            []
        )

        for handler in handlers:

            handler(event)