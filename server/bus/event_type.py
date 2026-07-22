from enum import Enum


class EventType(Enum):
    """
    Defines all server events.
    """


    CLIENT_MESSAGE = "client_message"


    PLAYER_CONNECTED = "player_connected"


    PLAYER_DISCONNECTED = "player_disconnected"


    USER_LOGIN = "user_login"


    ROOM_CREATED = "room_created"


    PLAYER_JOINED_ROOM = "player_joined_room"


    GAME_STARTED = "game_started"


    GAME_MOVE = "game_move"


    GAME_FINISHED = "game_finished"