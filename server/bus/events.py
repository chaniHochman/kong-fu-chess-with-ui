#המחלקה מייצגת אירוע פנימי שעובר בתוך השרת.
from enum import Enum



class EventType(Enum):
    """
    Defines all internal server events.
    """


    PLAYER_CONNECTED = "PLAYER_CONNECTED"


    PLAYER_DISCONNECTED = "PLAYER_DISCONNECTED"


    GAME_STARTED = "GAME_STARTED"


    GAME_ENDED = "GAME_ENDED"


    MOVE_REQUESTED = "MOVE_REQUESTED"


    MOVE_ACCEPTED = "MOVE_ACCEPTED"


    MOVE_REJECTED = "MOVE_REJECTED"


    BOARD_UPDATED = "BOARD_UPDATED"


    SCORE_UPDATED = "SCORE_UPDATED"


    PLAY_SOUND = "PLAY_SOUND"


    START_ANIMATION = "START_ANIMATION"


    END_ANIMATION = "END_ANIMATION"


    LOG_EVENT = "LOG_EVENT"