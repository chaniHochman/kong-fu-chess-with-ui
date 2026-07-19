#מחזיקה את מבנה ההודעות שעוברות בין:

# Client
# Server
import json

class Message:
    """
    Represents a message
    exchanged between client and server.
    """



    def __init__(self, message_type, payload):

        """
        Create a new message.

        message_type:
        Defines the action.

        payload:
        Contains message data.
        """

        self.type = message_type

        self.payload = payload



    def to_json(self):

        """
        Convert message object
        into JSON format.
        """


        return json.dumps(
            {
                "type": self.type,

                "payload": self.payload
            }
        )



    @staticmethod
    def from_json(data):

        """
        Create Message object
        from JSON string.
        """


        obj = json.loads(data)


        return Message(

            obj["type"],

            obj["payload"]

        )