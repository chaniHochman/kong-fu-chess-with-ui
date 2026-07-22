# הוא רק מתרגם הודעה → Event.

from server.bus.event import Event
from server.bus.event_type import EventType


class ClientCommandHandler:
    """
    Converts client messages
    into server events.

    Does not contain business logic.
    """


    # Creates command handler.
    def __init__(self, bus):

        self._bus = bus



    # Handles client message event.
    def handle(self, event):

        connection = event.data["connection"]

        message = event.data["message"]


        message_type = message.type

        payload = message.payload


        if message_type == MessageType.LOGIN:

            self._handle_login(
                connection,
                payload
            )


        elif message_type == MessageType.REGISTER:

            self._handle_register(
                connection,
                payload
            )

    # Creates login request event.
    def _handle_login(
        self,
        connection,
        payload
    ):

        self._bus.publish(
            Event(
                EventType.LOGIN_REQUEST,
                {
                    "connection": connection,
                    "username": payload["username"],
                    "password": payload["password"]
                }
            )
        )



    # Creates register request event.
    def _handle_register(
        self,
        connection,
        payload
    ):

        self._bus.publish(
            Event(
                EventType.REGISTER_REQUEST,
                {
                    "connection": connection,
                    "username": payload["username"],
                    "password": payload["password"]
                }
            )
        )



    # Creates room creation request event.
    def _handle_create_room(
        self,
        connection
    ):

        self._bus.publish(
            Event(
                EventType.CREATE_ROOM_REQUEST,
                {
                    "connection": connection
                }
            )
        )



    # Creates join room request event.
    def _handle_join_room(
        self,
        connection,
        payload
    ):

        self._bus.publish(
            Event(
                EventType.JOIN_ROOM_REQUEST,
                {
                    "connection": connection,
                    "room_id": payload["room_id"]
                }
            )
        )



    # Creates move request event.
    def _handle_move(
        self,
        connection,
        payload
    ):

        self._bus.publish(
            Event(
                EventType.MOVE_REQUESTED,
                {
                    "connection": connection,
                    "move": payload["move"]
                }
            )
        )



    # Creates matchmaking request event.
    def _handle_play(
        self,
        connection
    ):

        self._bus.publish(
            Event(
                EventType.MATCH_REQUEST,
                {
                    "connection": connection
                }
            )
        )