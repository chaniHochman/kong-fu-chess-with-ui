from enum import Enum


class EventType(Enum):
    """
    Defines all server events.
    """

    CLIENT_MESSAGE = "client_message"


    PLAYER_CONNECTED = "player_connected"


    PLAYER_DISCONNECTED = "player_disconnected"


    LOGIN_SUCCESS = "login_success"


    LOGIN_FAILED = "login_failed"


    REGISTER_FAILED = "register_failed"



    ROOM_CREATED = "room_created"


    PLAYER_JOINED_ROOM = "player_joined_room"


    ROOM_JOIN_FAILED = "room_join_failed"



    GAME_STARTED = "game_started"


    GAME_FINISHED = "game_finished"


    MOVE_ACCEPTED = "move_accepted"


    MOVE_REJECTED = "move_rejected"

    JOIN_ROOM_COMMAND = "join_room_command"