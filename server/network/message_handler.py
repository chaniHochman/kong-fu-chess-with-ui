
# מקשרת בין:
# WebSocket
# לבין:
# MessageBus
# היא מתרגמת:
# הודעה מהלקוח
# ↓
# אירוע פנימי
# ממיר הודעות רשת לאירועים פנימיים של השרת.
from common.events import Event, EventType



class MessageHandler:
    """
    Converts network messages
    into internal server events.
    """

    def __init__(self, bus):
        """
        Store MessageBus reference.
        """
        self.bus = bus


    def handle_message(self, message):

        """
        Convert client message
        into Event object.
        """

        if message["type"] == "MOVE":

            event = Event(

                EventType.MOVE_REQUESTED,

                message["data"]

            )


            self.bus.publish(event)